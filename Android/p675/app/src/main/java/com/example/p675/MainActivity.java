package com.example.p675;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;

import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.BitmapDescriptor;
import com.google.android.gms.maps.model.BitmapDescriptorFactory;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.MarkerOptions;

public class MainActivity extends AppCompatActivity {
    // 프래그먼트에 맵을 넣기위해 SupportMapFragment 객체 생성
    SupportMapFragment supportMapFragment;
    // GoogleMap 객체는 build.gradle에 googleMap 관련 API를 넣어줘야 사용할 수 있다.
    GoogleMap gmap;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // 맵프래그먼트 변수 초기화
        supportMapFragment = (SupportMapFragment)getSupportFragmentManager().findFragmentById(R.id.map);
        // 지도 콜백을 등록
        supportMapFragment.getMapAsync(new OnMapReadyCallback() {
            @Override
            public void onMapReady(GoogleMap googleMap) {
                gmap = googleMap;
                LatLng latLng = new LatLng(37.528352, 126.996073);
                gmap.addMarker(
                        new MarkerOptions().position(latLng).title("폴리텍").snippet("xxx").icon(BitmapDescriptorFactory.fromResource(R.drawable.d1)));
                // 해당 좌표로 카메라 이동
                gmap.animateCamera(CameraUpdateFactory.newLatLngZoom(latLng,10));

            }
        });
    }
    // 버튼 1을 누르면 월미도 좌표로 이동
    public void ck1(View v){
        LatLng latLng = new LatLng(37.472152, 126.602970);
        gmap.addMarker(
            new MarkerOptions().position(latLng).title("월미도").snippet("xxx").icon(BitmapDescriptorFactory.fromResource(R.drawable.d1)));
        gmap.animateCamera(CameraUpdateFactory.newLatLngZoom(latLng,15));

    }
    // 버튼 2를 누르면 김포국제공항 좌표로 이동
    public void ck2(View v){
        LatLng latLng = new LatLng(37.558867, 126.803048);
        gmap.addMarker(
            new MarkerOptions().position(latLng).title("김포국제공항").snippet("xxx").icon(BitmapDescriptorFactory.fromResource(R.drawable.d1)));
        gmap.animateCamera(CameraUpdateFactory.newLatLngZoom(latLng,20));
    }
}