package com.example.p475;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.widget.TextView;

import java.util.Random;

public class MainActivity extends AppCompatActivity {
    TextView    textView, textView2;
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

        Thread t = new Thread(new MyThread());
        Thread t2 = new Thread(new MyThread2());
        t.start();
        t2.start();
    }
    class MyThread extends Thread{
        Random random = new Random();
        @Override
        public void run(){
            for(int i=1; i <=200; i++ ){
                try{
                    Thread.sleep(500);

                }catch(InterruptedException e){
                    e.printStackTrace();
                }
                int randomValue1 = random.nextInt(200)+1;
                Message message = myHandler.obtainMessage();
                Bundle bundle = new Bundle();
                bundle.putInt("tdata",randomValue1);
                message.setData(bundle);
                myHandler.sendMessage(message);
            }
        }
    }

    class MyThread2 implements Runnable{
        Random random = new Random();
        @Override
        public void run() {
            for(int i=1;i<5000;i++){
                try {
                    Thread.sleep(500);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                int randomValue2 = random.nextInt(5000)+1;
                Message message2 = myHandler2.obtainMessage();
                Bundle bundle = new Bundle();
                bundle.putInt("tdata",randomValue2);
                message2.setData(bundle);
                myHandler2.sendMessage(message2);
            }
        }
    }

    class MyHandler extends Handler {
        @Override
        public void handleMessage(@NonNull Message msg) {
            Bundle bundle = msg.getData();
            int data = bundle.getInt("tdata",0);
            textView.setText("Handler1: "+data);
        }
    }
    class MyHandler2 extends Handler {
        @Override
        public void handleMessage(@NonNull Message msg) {
            Bundle bundle = msg.getData();
            int data = bundle.getInt("tdata",0);
            textView2.setText("Handler2:"+data);
        }

    }
}

