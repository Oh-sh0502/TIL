package com.example.p458;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;

public class MainActivity extends AppCompatActivity {
    WebView webView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        webView = findViewById(R.id.webView);

        // html을 렌더링 해준다.
        webView.setWebViewClient(new WebViewClient());
        // 안드로이드에 브라우저 기능을 가져온다.
        WebSettings webSettings = webView.getSettings();
        // 자바스크립트가 동작할 수 있는 환경으로 설정
        webSettings.setJavaScriptEnabled(true);
        String permisssions[] = {

        };
    }

    public void ckbt(View v){
        if(v.getId() == R.id.button){
            webView.loadUrl("http://m.naver.com");
        }else if (v.getId() == R.id.button2){
            webView.loadUrl("http://m.daum.net");
        }else if(v.getId() == R.id.button3){
            webView.loadUrl("http://192.168.0.21");
        }
    }

}