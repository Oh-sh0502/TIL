package com.example.p251;

import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        String [] permissions = {};
        ActivityCompat.requestPermissions(this,permissions,101);
    }
    public void ckbt(View view){
        Intent intent =
                new Intent(getApplicationContext(), SecondActivity.class);

        intent.putE


    }
}