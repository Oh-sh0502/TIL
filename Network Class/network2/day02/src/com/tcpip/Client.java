package com.tcpip;

import java.io.BufferedWriter;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.Scanner;

public class Client {

	int port;
	String ip;
	DataOutputStream ow = null;
	Socket socket;

	public Client(String ip, int port) {
		this.ip = ip;
		this.port = port;
	}

	public void connectServer() {
		try {
			System.out.println("Start Client");
			socket = new Socket(ip, port);
			System.out.println("Connected ...");
		} catch (Exception e) {
			while (true) {
				try {
					Thread.sleep(2000);
					socket = new Socket(ip, port);
					System.out.println("Connected ...");
					break;
				} catch (Exception e1) {
					System.out.println("Re Try ...");
				}
			}
		}
	}

	public void request(String msg) throws IOException {

		connectServer();

		try {
			ow = new DataOutputStream(socket.getOutputStream());
			// bw = new BufferedWriter(ow);
			ow.writeUTF(msg);
		} catch (Exception e) {
			throw e;
		} finally {

		}
	}

	public void close() throws IOException {
		if (ow != null) {
			ow.close();
		}
		if (socket != null) {
			socket.close();
		}
	}

	public static void main(String[] args) {
		Client client = null;
		client = new Client("192.168.0.36", 9999);
		// client.connectServer();

		Scanner sc = new Scanner(System.in);
		while (true) {
			System.out.println("Input msg");
			String msg = sc.nextLine();
			if (msg.equals("q")) {
				try {
					client.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
				break;
			}
			try {
				client.request(msg);
			} catch (IOException e) {
				e.printStackTrace();
			}
		}

		System.out.println("End Client");
	}

}
