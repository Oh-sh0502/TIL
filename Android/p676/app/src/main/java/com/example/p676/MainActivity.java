package com.example.p676;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;

import android.Manifest;
import android.annotation.SuppressLint;
import android.content.Context;
import android.content.pm.PackageManager;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.os.Bundle;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.BitmapDescriptorFactory;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.MarkerOptions;

import org.w3c.dom.Text;

public class MainActivity extends AppCompatActivity {
    TextView textView;
    LocationManager locationManager;

    SupportMapFragment supportMapFragment;
    GoogleMap gmap;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        getSupportActionBar().hide();

        String [] permission = {
                Manifest.permission.ACCESS_FINE_LOCATION,
                Manifest.permission.ACCESS_COARSE_LOCATION
        };
        ActivityCompat.requestPermissions(this,
                permission,101);

        supportMapFragment = (SupportMapFragment)getSupportFragmentManager().findFragmentById(R.id.map);
        supportMapFragment.getMapAsync(new OnMapReadyCallback() {
            @Override
            public void onMapReady(GoogleMap googleMap) {
                gmap = googleMap;
                if(checkSelfPermission(Manifest.permission.ACCESS_FINE_LOCATION)== PackageManager.PERMISSION_DENIED||
                        checkSelfPermission(Manifest.permission.ACCESS_COARSE_LOCATION)== PackageManager.PERMISSION_DENIED){
                    // 앱을 종료한다.
                    return;
                }
                gmap.setMyLocationEnabled(true);
                LatLng latLng = new LatLng(37.528352, 126.996073);
                gmap.addMarker(
                        new MarkerOptions().position(latLng).title("폴리텍").snippet("xxx"));
                gmap.animateCamera(CameraUpdateFactory.newLatLngZoom(latLng,10));
            }
        });

        // Location
        textView = findViewById(R.id.textView);
        // 로케이션 매니저를 사용하기 위해서는 액세스 파인로케이션이 필요함

        MyLocation myLocation = new MyLocation();
        locationManager =(LocationManager)getSystemService(Context.LOCATION_SERVICE);
        locationManager.requestLocationUpdates(
                LocationManager.GPS_PROVIDER,
                1,
                0,
                myLocation
        );

    }

    class MyLocation implements LocationListener {

        @Override
        public void onLocationChanged(@NonNull Location location) {
            double lat = location.getLatitude();
            double lon = location.getLongitude();
            textView.setText(lat+" "+lon);
            LatLng latLng = new LatLng(lat,lon);
//            gmap.addMarker(
//                    new MarkerOptions().position(latLng).
//                            title("현재 위치").snippet("xxx"));
//            gmap.animateCamera(CameraUpdateFactory.newLatLngZoom(latLng,10));
        }
    }

    // 앱을 다시 실행시키면 내용을 가져온다.
    @SuppressLint("MissingPermission")
    @Override
    protected void onPostResume() {
        super.onPostResume();
        if(gmap != null){
            gmap.setMyLocationEnabled(true);
        }
    }
    // 앱을 잠깐 꺼놓으면 기능 정지
    @SuppressLint("MissingPermission")
    @Override
    protected void onPause() {
        super.onPause();
        if(gmap != null){
            gmap.setMyLocationEnabled(false);
        }
    }
}