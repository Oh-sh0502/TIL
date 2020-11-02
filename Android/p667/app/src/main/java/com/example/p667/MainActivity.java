package com.example.p667;

import androidx.annotation.NonNull;
import androidx.annotation.RequiresApi;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;

import android.Manifest;
import android.content.Context;
import android.content.pm.PackageManager;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.os.Build;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;
import android.widget.Toast;

import org.w3c.dom.Text;

public class MainActivity extends AppCompatActivity {
    TextView textView;
    // 위치를 가져오기 위해 필요한 로케이션매니저
    LocationManager locationManager;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        textView = findViewById(R.id.textView);
        // 로케이션 매니저를 사용하기 위해서는 액세스 파인로케이션(위치 허용)이 필요함
        String [] permission = {
                Manifest.permission.ACCESS_FINE_LOCATION
        };
        // 권한 요청
        ActivityCompat.requestPermissions(this,
                // 권한 대상
                permission,
                // 요청코드
                101);
        // checkSelfPermission으로 권한을 체크한다. (여기에선 거부되면 앱을 종료시키는 코드)
        if(checkSelfPermission(Manifest.permission.ACCESS_FINE_LOCATION) == PackageManager.PERMISSION_DENIED){
            Toast.makeText(this,"Finish",Toast.LENGTH_SHORT).show();
            // 앱을 종료한다.
            finish();
        }
        // MyLocation이란 객체 선언 (밑에 MyLocation이라는 클래스 정의 필요)
        MyLocation myLocation = new MyLocation();
        // Context 클래스 안에 LOCATION_SERVICE는 GPS를 통한 위치서비스를 제공한다.
        locationManager =(LocationManager)getSystemService(Context.LOCATION_SERVICE);
        // 기기의 위치에 관한 정기 업데이트를 요청
        locationManager.requestLocationUpdates(
                /*위치정보를 구합니다.
                GPS Provider: 3각 측량의 방법으로 좌표를 위성을 이용하여 취득. 실내에서 사용이 어렵
                Network Provider: 이동통신 기지국 또는 WiFi  access point들을 이용하여 측정
                Passive Provider: 표를 직접 구하는 것이 아니고 다른 어플리케이션이나 서비스가 좌표 값을
                                  구하면 단순히 그 값을 받아 오기만 하는 전달자 역할*/
                LocationManager.GPS_PROVIDER,
                // 입력한 시간마다 변동이 있으면 업데이트합니다.
                1,
                // 입력한 거리마다 변동이 있으면 업데이트합니다.
                0,
                // MyLocation 객체 변수 myLocation실행
                myLocation
        );
    }


    // MyLocation 객체 정의 -> 위치리스너. 이벤트가 발생하면 연결된 리스너(핸들러)들에게 이벤트를 전달한다
    class MyLocation implements LocationListener{
        // 변동된 위치를 받는다.
        @Override
        public void onLocationChanged(@NonNull Location location) {
            // 위도
            double lat = location.getLatitude();
            // 경도
            double lon = location.getLongitude();
            // 텍스트뷰에 반영
            textView.setText(lat+" "+lon);
        }
    }

    // 버튼을 누르면 함수발동
    public void ck(View v){
        startMyLocation();
    }

    // 내 위치를 알려줘 함수
    private void startMyLocation(){
        Location location = null;
        if(checkSelfPermission(Manifest.permission.ACCESS_FINE_LOCATION) == PackageManager.PERMISSION_DENIED){
            Toast.makeText(this,"Finish",Toast.LENGTH_SHORT).show();
            // 앱을 종료한다.
            finish();
        }
        location = locationManager.getLastKnownLocation(
                LocationManager.GPS_PROVIDER
        );
        if(location != null){

            double lat = location.getLatitude();
            double lon = location.getLongitude();
            textView.setText((lat+" "+lon));
        }
    }


}