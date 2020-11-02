package com.example.p474;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.app.ProgressDialog;
import android.content.DialogInterface;
import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.view.View;
import android.widget.Button;
import android.widget.ProgressBar;
import android.widget.TextView;

import org.w3c.dom.Text;

public class MainActivity extends AppCompatActivity {
    ProgressBar progressBar, progressBar2;
    TextView textView, textView2;
    Button button,button2,button3;
    MyHandler myHandler;
    MyHandler2 myHandler2;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        progressBar = findViewById(R.id.progressBar);
        progressBar2 = findViewById(R.id.progressBar2);
        progressBar.setMax(50);
        progressBar2.setMax(50);
        textView = findViewById(R.id.textView);
        button = findViewById(R.id.button);
        button2 = findViewById(R.id.button2);
        button3 = findViewById(R.id.button3);
        textView2 = findViewById(R.id.textView2);
        myHandler = new MyHandler();
        myHandler2 = new MyHandler2();

    }

    public void ckbt(View v) {
        if(v.getId() == R.id.button){
            Thread t = new Thread(new MyThread());
            t.start();
            button.setEnabled(false);
        }else if(v.getId() == R.id.button2){
            Thread t = new Thread(new MyThread2());
            t.start();
            button.setEnabled(false);
        }else if(v.getId() == R.id.button3){
            progress();
        }
    }

    public void progress(){
        ProgressDialog progressDialog = new ProgressDialog(this);
        AlertDialog.Builder dialog = new AlertDialog.Builder(this);
        dialog.setTitle("progress");
        dialog.setMessage("5 second");
        Handler handler = new Handler();
        dialog.setPositiveButton("ok", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                progressDialog.setCancelable(true);
                progressDialog.setTitle("Downloading ...");
                progressDialog.show();
                handler.postDelayed(new Runnable() {
                    @Override
                    public void run() {
                        progressDialog.dismiss();
                    }
                }, 5000);
            }
        });
        dialog.show();
    }

    // Thread t = new Thread(){};
    class MyThread extends Thread{
        @Override
        public void run() {
            for(int i=1;i<50;i++){
                progressBar.setProgress(i);
                textView.setText(i+"");
                try {
                    Thread.sleep(200);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                runOnUiThread(new Runnable(){

                    @Override
                    public void run() {
                        button.setEnabled(true);
                    }
                });
                button.setEnabled(true);

            }
        }
    }

    class MyHandler extends Handler {
        @Override
        public void handleMessage(@NonNull Message msg) {
            Bundle bundle = msg.getData();
            int data = bundle.getInt("tdata",0);
            textView.setText("Handler1: "+data);
            progressBar.setProgress(data);
        }
    }
    class MyHandler2 extends Handler {
        @Override
        public void handleMessage(@NonNull Message msg) {
            Bundle bundle = msg.getData();
            int data = bundle.getInt("tdata",0);
            textView2.setText("Handler2:"+data);
            progressBar2.setProgress(data);
            if(data == 49){
                button2.setEnabled(true);
            }

        }
    }


    class MyThread2 implements Runnable{

        @Override
        public void run() {
            for(int i=1;i<50;i++){
                try {
                    Thread.sleep(100);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                Message message = myHandler.obtainMessage();
                Message message2 = myHandler2.obtainMessage();
                Bundle bundle = new Bundle();
                bundle.putInt("tdata",100);
                message.setData(bundle);
                message2.setData(bundle);
                myHandler.sendMessage(message);
                myHandler2.sendMessage(message2);
            }
        }
    }
}