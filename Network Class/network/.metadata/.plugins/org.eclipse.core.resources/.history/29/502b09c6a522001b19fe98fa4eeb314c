package com.tcpip;

import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.ServerSocket;
import java.net.Socket;

public class Server {
	int port = 9999;
	ServerSocket serverSocket;
	Socket socket;
	
	DataInputStream ir;
	BufferedReader br;
	
	public Server() {
		
	}
	public void startServer() throws IOException {
		serverSocket = new ServerSocket(port);
		try {
			while(true) {
				System.out.println("Ready Server ...");
				socket = serverSocket.accept();
				System.out.println("Connected ...");
				ir = new DataInputStream(socket.getInputStream());
				//br = new BufferedReader(ir);
				String msg = "";
				msg = ir.readUTF();
				System.out.println(msg);
			}
		}catch(Exception e) {
			throw e;
		}finally {
//			if(br != null) {
//				br.close();
//			}
			if(socket != null) {
				socket.close();
			}
		}
	}
	
	public static void main(String[] args) {
		Server server = null;
		server = new Server();
		try {
			server.startServer();
		} catch (IOException e) {
			e.printStackTrace();
		}
		System.out.println("End Server");
	}

}
