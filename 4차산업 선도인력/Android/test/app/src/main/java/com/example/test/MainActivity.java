package com.example.test;

import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;
import androidx.core.content.PermissionChecker;

import android.Manifest;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        String [] permissions = {
                Manifest.permission.CALL_PHONE
        };
        ActivityCompat.requestPermissions(
                this,permissions,101
        );

    }
    public void ck(View v){
        Intent intent = null;

        int check =
                PermissionChecker.checkSelfPermission(
                        this,Manifest.permission.CALL_PHONE
                );
        if(check == PackageManager.PERMISSION_GRANTED){
            intent = new Intent(Intent.ACTION_CALL,
                    Uri.parse("tel:010-2233-2323"));
        }else{
            return;
        }
        startActivity(intent);
    }
}