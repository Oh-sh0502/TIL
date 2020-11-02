package com.example.p489;

import androidx.appcompat.app.AppCompatActivity;

import android.os.AsyncTask;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.SeekBar;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    Button button, button2;
    SeekBar seekBar;
    TextView textView;
    ImageView imageView;
    MyAsynch myAsynch;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        button = findViewById(R.id.button);
        button2 = findViewById(R.id.button2);
        seekBar = findViewById(R.id.seekBar);
        seekBar.setMax(100);
        textView = findViewById(R.id.textView);
        imageView = findViewById(R.id.imageView);
        button.setEnabled(true);
        button2.setEnabled(false);
    }

    public void ckbt1(View v){
        myAsynch = new MyAsynch();
        myAsynch.execute(10);                 //doInBackground로~
    }
    public void ckbt2(View v){
        myAsynch.cancel(true);
        myAsynch.onCancelled();
    }

    class MyAsynch extends AsyncTask<Integer, Integer,String> {
        @Override
        protected void onPreExecute() {
            button.setEnabled(false);
            button2.setEnabled(true);
        }

        @Override
        protected String doInBackground(Integer... integers) {
            int a = integers[0].intValue();
            int sum = 0;
            for(int i =0; i<100; i++){
                if(isCancelled() == true){
                    break;
                }
                sum += i;
                // onProgressUpdate로 던짐
                publishProgress(i);
                try {
                    Thread.sleep(100);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            return "age: " +sum ;

        }

        // doInBackground에서 던지는걸 받음
        @Override
        protected void onProgressUpdate(Integer... values) {
            int i = values[0].intValue();
            seekBar.setProgress(i);
            if(i<=30){
                imageView.setImageResource(R.drawable.young);
            }else if(i <= 70){
                imageView.setImageResource(R.drawable.old);
            }else if(i <= 100){
                imageView.setImageResource(R.drawable.tooold);
            }
            textView.setText("age:" + i);

        }

        // MyAsynch가 끝나고 리턴되는 스트링이 여기로 옴
        @Override
        protected void onPostExecute(String s) {
            textView.setText("나이의 총합(?):" + s);
            button.setEnabled(true);
            button2.setEnabled(false);
            // 텍스트 뷰에 출력
//            textView.setText(s);
        }

        @Override
        protected void onCancelled() {
            seekBar.setProgress(0);
            textView.setText("");
            imageView.setImageResource(R.drawable.d1);
            button.setEnabled(true);
            button2.setEnabled(false);


        }
    }
}