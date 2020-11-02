package com.tcpip;

import java.io.DataInputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class Server {

	int port;
	// ��� ����
	ServerSocket serverSocket;
	Socket socket;
	
	
	// �⺻ ������
	public Server() {}
	
	// ��Ʈ�� �޴� ������
	public Server(int port) {
		this.port = port;
	}
	
	// Ŭ���̾�Ʈ�� ������ �޴� ������ ����(Ŭ���̾�Ʈ�� ���������� ����: ��ǲ��Ʈ��)
	class Receiver extends Thread{
		DataInputStream dis;
		Socket socket;
		public Receiver(Socket socket) {
			this.socket = socket;
			try {
				dis = new DataInputStream(socket.getInputStream());
			} catch (IOException e) {
				
				e.printStackTrace();
			}
		}
		
		// �޾ƿͼ� ó��
		@Override
		public void run() {
			while(dis != null) {
				String msg = "";
				try {
					msg = dis.readUTF();
					// Ŭ���̾�Ʈ�� q �Է½�
					if(msg.equals("q")) {
						System.out.println("Ŭ���̾�Ʈ�� �������ϴ�.");
						break;
					}
					System.out.println(msg);
				} catch (IOException e) {
					// Ŭ���̾�Ʈ�� �׳� ������ ��������� ��
					System.out.println("Ŭ���̾�Ʈ�� �������ϴ�.");
					break;
				}
			}
			
			if(dis != null) {
				try {
					dis.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
			if(socket != null) {
				try {
					socket.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
		}
	}
	
	// ���� ���� �Լ�. ������ �����ϸ� ���� ������ ��������鼭 ���Ʈ�� ��ٸ��� �������� ������ ������ �����Ѵ�.
	public void startServer() throws Exception {
		System.out.println("TCP/IP Server Start ...");
		// Exception �� �Ͼ�� �� ��ó�� �� �ִ� ����
		try {
			serverSocket = new ServerSocket(port);
			// ������ �������� �����ʰ� ����־�� �ϹǷ� ����
			while(true) {
				System.out.println("Ready Server ..");
				// Ŭ���̾�Ʈ�� �ް� �Ǹ鼭 ������ ����.
				socket = serverSocket.accept();
				// Ŭ���̾�Ʈ�� �巯���� ����Ǿ��ٰ� ���
				System.out.println("Connected ...");
				new Receiver(socket).start();
			}
		}catch(Exception e) {
			throw e; 
		}
		
	}
	
	
	public static void main(String[] args) {
		Server server = new Server(7777);
		try {
			server.startServer();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

}
