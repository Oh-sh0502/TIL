package com.example.fire;

import android.app.Service;
import android.content.Intent;
import android.os.IBinder;
import android.util.Log;

import androidx.annotation.NonNull;
import androidx.core.app.NotificationManagerCompat;
import androidx.localbroadcastmanager.content.LocalBroadcastManager;

import com.google.firebase.messaging.FirebaseMessagingService;
import com.google.firebase.messaging.RemoteMessage;

public class MyFService extends FirebaseMessagingService {
    String TAG = "===";

    String carId, control, data;

    NotificationManagerCompat notificationManager;


    public MyFService() {
        Log.d("-------------------", "MyFService : " );

    }
    @Override
    public void onMessageReceived(@NonNull RemoteMessage remoteMessage) {
        carId = remoteMessage.getNotification().getTitle();
        control = remoteMessage.getData().get("control");
        data = remoteMessage.getData().get("data");
        Log.d(TAG, "carId : " + carId + " | control : " + control + " | data : " + data);
        Intent intent = new Intent("filter_string");
        // put your all data using put extra

        intent.putExtra("carId", carId);
        intent.putExtra("control", control);
        intent.putExtra("data", data);
        LocalBroadcastManager.getInstance(this).sendBroadcast(intent);
    }
    @Override
    public void onNewToken(@NonNull String s) {
        super.onNewToken(s);
    }
}
