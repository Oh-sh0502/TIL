package com.example.base;

import android.app.Service;
import android.content.Intent;
import android.os.IBinder;
import android.util.Log;

import androidx.annotation.NonNull;
import androidx.localbroadcastmanager.content.LocalBroadcastManager;

import com.google.firebase.messaging.FirebaseMessagingService;
import com.google.firebase.messaging.RemoteMessage;

public class MyFireService extends FirebaseMessagingService {

    String carId, control, data;
    String TAG = "=====";
    public MyFireService() {
        Log.d("----------------", "MyFService");

    }

    @Override
    public void onMessageReceived(@NonNull RemoteMessage remoteMessage) {
        carId = remoteMessage.getNotification().getTitle();
        control = remoteMessage.getData().get("control");
        data = remoteMessage.getData().get("data");
        Log.d(TAG, "carId : " + carId + " | control : " + control + " | data : " + data);
     }

}
