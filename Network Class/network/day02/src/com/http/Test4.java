package com.http;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;

public class Test4 {

	public static void main(String[] args) {
		String urlstr = "http://192.168.0.36/network/login.jsp";
		URL url = null;
		HttpURLConnection con = null;

		BufferedReader br = null;

		try {
			
			url = new URL(urlstr + "?id=qqq&pwd=111");
			con = (HttpURLConnection) url.openConnection();
			con.setReadTimeout(5000);
			con.setRequestMethod("POST");
			con.getInputStream();

			br = new BufferedReader(
					new InputStreamReader(
							con.getInputStream()));

			String str = "";
			//str = br.readLine();
			//System.out.println(str);
			while ((str = br.readLine()) != null) {
				if(str.equals("")) {
					continue;
				}
				System.out.println(str.trim());
			}

		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			con.disconnect();
			if (br != null) {
				try {
					br.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}

		}

	}

}
