package com.tcpip;

import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;

import javax.servlet.http.HttpServletResponse;

import org.json.simple.JSONObject;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import com.chat.Client;

@Controller
public class MainController {
	Client client;
	
	public MainController() {
		client = new Client("13.124.204.170", 5555, "[WEB]");
		try {
			client.connect();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	
	
	@RequestMapping("/main.mc")
	public ModelAndView main() {
		ModelAndView mv = new ModelAndView();
		mv.setViewName("main");
		return mv;
	}
	
	@RequestMapping("/iot.mc")
	public void iot(HttpServletResponse res) throws IOException {
		System.out.println("IoT Send Start ...");
		client.sendTarget("/192.168.25.57","100");
		
		URL url = null;
		try {
			url = new URL("https://fcm.googleapis.com/fcm/send");
		} catch (MalformedURLException e) {
			System.out.println("Error while creating Firebase URL | MalformedURLException");
			e.printStackTrace();
		}
		HttpURLConnection conn = null;
		try {
			conn = (HttpURLConnection) url.openConnection();
		} catch (IOException e) {
			System.out.println("Error while createing connection with Firebase URL | IOException");
			e.printStackTrace();
		}
		conn.setUseCaches(false);
		conn.setDoInput(true);
		conn.setDoOutput(true);
		conn.setRequestProperty("Content-Type", "application/json");

		// set my firebase server key
		conn.setRequestProperty("Authorization", "key="
				+ "AAAAXsC9rSI:APA91bErxOelV8P8C02sDT8-fRifuKxoRcw7KXhyLteJqIpFB7n3Vm4hOKIA_tbNP-8e15_4tGN3cZFKIqN7I1JcbpBl6-wc1Wbn4w97ONfI0IMeSkrRoauqg8lOUcuH0PfxfJbjLrbN"); 

		// create notification message into JSON format
		JSONObject message = new JSONObject();
		message.put("to", "/topics/car");
		message.put("priority", "high");
		JSONObject notification = new JSONObject();
		notification.put("title", "�̺�Ʈ");
		notification.put("body", "����! 50% ��ȭ �������� �߼�!");
		message.put("notification", notification);
		
		JSONObject data = new JSONObject();
		data.put("control", "control1");
		data.put("data", 100);
		message.put("data", data);


		try {
			OutputStreamWriter out = new OutputStreamWriter(conn.getOutputStream(), "UTF-8");
			out.write(message.toString());
			out.flush();
			conn.getInputStream();
			System.out.println("OK...............");

		} catch (IOException e) {
			System.out.println("Error while writing outputstream to firebase sending to ManageApp | IOException");
			e.printStackTrace();
		}	

		
		PrintWriter out = res.getWriter();
		out.print("ok");
		out.close();
	}

	@RequestMapping("/phone.mc")
	public void phone() {
		System.out.println("Phone Send Start ...");
	}
}