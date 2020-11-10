package com.tcpip;

import java.net.Socket;

public class Client {

	int port;
	String ip;
	Socket socket;
	
	public Client(String ip,int port) {
		this.ip = ip;
		this.port = port;
	}
	
	public void connectServer() {
		try {
			System.out.println("Start Client");
			socket = new Socket(ip, port);
			System.out.println("Connected ...");
		} catch (Exception e) {
			e.printStackTrace();
		} 
	}
	
	public static void main(String[] args) {
		Client client = null;
		client = new Client("192.168.0.36",9999);
		client.connectServer();
		
		System.out.println("End Client");
	}

}






