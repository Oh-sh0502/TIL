package com.example.p217;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.app.ProgressDialog;
import android.content.DialogInterface;
import android.os.Bundle;
import android.view.Gravity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ProgressBar;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.material.snackbar.Snackbar;

public class MainActivity extends AppCompatActivity {               //MainActivity는 현재 판때기를 의미

    ProgressBar progressBar;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        progressBar = findViewById(R.id.progressBar);
        progressBar.setMax(10);
    }

    // 첫번째 버튼: 중앙에 토스트 띄우기
    public void clickb1(View v){
        Toast t = Toast.makeText(this,"Toast1 ...", Toast.LENGTH_SHORT);
        t.setGravity(Gravity.CENTER,0,0);
        t.show();
    }

    // 두번째 버튼: 다른 xml 띄우기
    public void clickb2(View v){
        // inflater는 xml로 정의된 view (또는 menu 등)를 실제 객체화 시키는 용도입니다.
        LayoutInflater inflater = getLayoutInflater();
        // toast.xml을 객체화해서 View 객체 view 변수에 가져옵니다.
        View view = inflater.inflate(R.layout.toast,
                (ViewGroup) findViewById(R.id.toast_layout));
        // id가 textView인 텍스트뷰를 TextView 객체 tv 변수에 저장
        TextView tv = view.findViewById(R.id.textView);
        // 텍스트뷰 tv에 "INPUT TEXT" 라는 문구를 박는다.
        tv.setText("INPUT TEXT");

        Toast t = new Toast(this);
        t.setGravity(Gravity.CENTER,0,0);
        t.setDuration(Toast.LENGTH_LONG);
        t.setView(view);
        t.show();
    }

    // 세번째 버튼: 스낵바
    public void clickb3(View v){
        Snackbar.make(v, "Snack Bar", Snackbar.LENGTH_LONG).show();
    }

    // 네번째 버튼: 다이얼로그 띄우기
    public void clickb4(View v){
        AlertDialog.Builder builder = new AlertDialog.Builder(this);
        builder.setTitle("My Dialog");
        builder.setMessage("Are You Exit Now");
        builder.setIcon(R.drawable.ic_launcher_background);

        builder.setPositiveButton("Cancel", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                finish();
            }
        });
        builder.setNegativeButton("NO", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {

            }
        });
        AlertDialog dialog = builder.create();
        dialog.show();
    }

    public void btprogress(View v){
        ProgressDialog progressDialog = null;
        if(v.getId() == R.id.button5){
            int pdata = progressBar.getProgress();
            if(pdata < 10){
                progressBar.setProgress(pdata + 1);
            }else{
                Toast.makeText(this, "Max Value",
                        Toast.LENGTH_SHORT).show();
            }
        }else if (v.getId() ==R.id.button6){
            int pdata = progressBar.getProgress();
            progressBar.setProgress(pdata - 1);
        }else if (v.getId() == R.id.button7){
            progressDialog = new ProgressDialog(this);
            progressDialog.setProgressStyle(ProgressDialog.STYLE_SPINNER);
            progressDialog.setTitle("Downloading ...");
            progressDialog.setCancelable(false);                                // 이게 있으면 다운로드화면에서 바깥 눌러도 안나가짐ㄴ
            progressDialog.show();
        }else if (v.getId() == R.id.button8){
            progressDialog.dismiss();
        }
    }




    @Override
    public void onBackPressed() {
        // 화면 띄우기
        LayoutInflater inflater = getLayoutInflater();
        View view = inflater.inflate(R.layout.toast,
                (ViewGroup) findViewById(R.id.toast_layout));

        AlertDialog.Builder builder = new AlertDialog.Builder(this);
        builder.setTitle("My Dialog");
        builder.setMessage("Are You Exit Now");
        builder.setIcon(R.drawable.ic_launcher_background);

        builder.setPositiveButton("OK", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {

            }
        });
        AlertDialog dialog = builder.create();
        dialog.show();



    }
}   // end class