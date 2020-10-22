package com.example.p207;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.res.Configuration;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
    // 객체 생성
    Button button;                      // 버튼
    EditText et;                        // 에디트텍스트
    TextView textView;                  // 텍스트뷰
    String str;                         // 스트링

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        // 앱 시작시 "onCreate" 보여짐
        show("onCreate");
        Log.d("[TEST]","onStart");                                                       // 확인용 로그
        button = findViewById(R.id.button);
        et = findViewById(R.id.et);
        textView = findViewById(R.id.textView2);
//        Toast.makeText(MainActivity.this, str,Toast.LENGTH_SHORT).show();

        // 버튼 이벤트 처리
//        button.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View v) {
//                str = et.getText().toString();                                                    // getText()는 editable 이기 때문에 toString을 사용하여 string으로 바꿔줘야 한다.
//                Toast.makeText(MainActivity.this, str,Toast.LENGTH_SHORT).show();         // LENGTH_SHORT: 몇 초동안 띄울거냐를 의미. SHORT는 2초, LONG은 3.5초
//                                                                                                  // show() 를 안하면 안 보여진다.
//            }
//        });
    }

    @Override
    public void onConfigurationChanged(@NonNull Configuration newConfig) {
        super.onConfigurationChanged(newConfig);
        if(newConfig.orientation == Configuration.ORIENTATION_LANDSCAPE){
            // 돌릴때 화면을 재조정
            setContentView(R.layout.activity_main);
//            Toast.makeText(this, "LANDSCAPE", Toast.LENGTH_SHORT).show();
        }else if(newConfig.orientation == Configuration.ORIENTATION_PORTRAIT) {
            // 화면 재조정
            setContentView(R.layout.activity_main);
//            Toast.makeText(this, "PORTRAIT", Toast.LENGTH_SHORT).show();
        }
    }

    @Override
    protected void onStart() {
        super.onStart();
        show("onStart");
        Log.d("[TEST]","onStart");
    }

    @Override
    protected void onStop() {
        super.onStop();
        show("onStop");
        Log.d("[TEST]","onStart");
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        show("onDestroy");
        Log.d("[TEST]","onStart");
    }

    public void show(String str){
        Toast.makeText(this,str,Toast.LENGTH_SHORT).show();
    }
}