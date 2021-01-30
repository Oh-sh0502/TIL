package com.example.p475;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.widget.TextView;

import org.w3c.dom.Text;

import java.util.Random;

public class MainActivity extends AppCompatActivity {
    TextView textView,textView2;
    MyHandler myHandler;
    MyHandler2 myHandler2;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        textView = findViewById(R.id.textView);
        textView2 = findViewById(R.id.textView2);
        myHandler = new MyHandler();
        myHandler2 = new MyHandler2();
        new Thread1().start();
        new Thread2().start();
    }
    class MyHandler extends Handler {
        @Override
        public void handleMessage(@NonNull Message msg) {
            Bundle bundle = msg.getData();
            int data = bundle.getInt("kdata",0);
            textView.setText(data+"km");
        }
    }
    class MyHandler2 extends Handler{
        @Override
        public void handleMessage(@NonNull Message msg) {
            Bundle bundle = msg.getData();
            int data = bundle.getInt("rdata",0);
            textView2.setText(data+"rpm");
        }
    }
    class Thread1 extends Thread{

        @Override
        public void run() {
            for(int i=0;i<=5000;i++){
                Random r = new Random();
                int kdata = r.nextInt(200)+1;
                Message message = myHandler.obtainMessage();
                Bundle bundle = new Bundle();
                bundle.putInt("kdata",kdata);
                message.setData(bundle);
                myHandler.sendMessage(message);
                try {
                    Thread.sleep(100);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }
    }

    class Thread2 extends Thread{

        @Override
        public void run() {
            for(int i=0;i<=5000;i++) {
                Random r = new Random();
                int rdata = r.nextInt(5000)+1;
                Message message = myHandler2.obtainMessage();
                Bundle bundle = new Bundle();
                bundle.putInt("rdata", rdata);
                message.setData(bundle);
                myHandler2.sendMessage(message);
                try {
                    Thread.sleep(100);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}










