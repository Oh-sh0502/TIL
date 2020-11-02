package com.example.p287;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

public class Fragment1 extends Fragment {

    TextView textView;
    EditText editText;
    Button button4;
    ImageView imageView;

    public Fragment1(){}

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        ViewGroup viewGroup = null;
        viewGroup = (ViewGroup)inflater.inflate(
                R.layout.fragment_1,container,false);
        viewGroup.findViewById(R.id.textView);
        viewGroup.findViewById(R.id.editText);
        viewGroup.findViewById(R.id.button4);
        imageView.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
                String str = editText.getText().toString();
                textView.setText(str);
            }
        });

        return viewGroup;

    }

    public void setTx(String str){
        textView.setText(str);
    }

}
