package com.example.myapplication;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.content.DialogInterface;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.CalendarView;
import android.widget.ImageView;
import android.widget.TextView;

import java.sql.Timestamp;
import java.text.SimpleDateFormat;
import java.util.Locale;

public class MainActivity extends AppCompatActivity {
    TextView textView;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        textView = findViewById(R.id.textView);
    }
    public void ckbt(View v){
        AlertDialog.Builder builder =
                new AlertDialog.Builder(MainActivity.this);

        LayoutInflater layoutInflater = getLayoutInflater();
        View dview = layoutInflater.inflate(R.layout.cal,
                (ViewGroup) findViewById(R.id.dlayout) );
        final CalendarView calendarView = dview.findViewById(R.id.calendarView);
        builder.setView(dview);

        builder.setTitle("Hi");

        builder.setPositiveButton("YES", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                long d = calendarView.getDate();
                SimpleDateFormat timeStampFormat = new SimpleDateFormat("yy-MM-dd HH:mm:ss",
                        Locale.KOREA);

                String date = timeStampFormat.format(new Timestamp(d));

                textView.setText(date);
            }
        });
        builder.setNegativeButton("NO", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {

            }
        });

        builder.show();
    }
}