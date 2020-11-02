# 맵을 가져오기 전에

1. build.gradle 에 googleMap 관련 API cnrk - sync now

  ```
  implementation 'com.google.android.gms:play-services-maps:17.0.0'
  ```

2. androidmanifest.xml 에 키 값 입력 
  ```
   <meta-data
          android:name="com.google.android.geo.API_KEY"
          android:value="AIzaSyD0PzgOynxwsTZGwDToQVgB6ojqrldjLYA"/>
  ```

3. 화면에 Fragment 추가

    ```
    <fragment
        android:id="@+id/map"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:name="com.google.android.gms.maps.SupportMapFragment"/>
    ```

    