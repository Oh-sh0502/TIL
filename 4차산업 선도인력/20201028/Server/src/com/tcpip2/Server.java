package com.tcpip2;

import java.io.IOException;
import java.io.ObjectInputStream;
import java.net.ServerSocket;
import java.net.Socket;

import com.msg.Msg;

// Object Serialization

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
		// object ���� ���� ObjectInputStream
		ObjectInputStream dis;
		Socket socket;
		public Receiver(Socket socket) {
			this.socket = socket;
			try {
				dis = new ObjectInputStream(socket.getInputStream());
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
		
		// �޾ƿͼ� ó��
		@Override
		public void run() {
			while(dis != null) {
				Msg mo = null;
				// object ��ü ����
				try {
					// object�� ���� ���� �̷���!
					mo = (Msg) dis.readObject();
					System.out.println(mo.getId()+mo.getIp()+mo.getMsg());
					dis = new ObjectInputStream(socket.getInputStream());
					if(mo.getMsg().equals("q")) {
						System.out.println(mo.getId()+"���� �������ϴ�.");
						break;
					}
					System.out.println(mo.getId()+":"+mo.getMsg());
				} catch (Exception e) {
					// Ŭ���̾�Ʈ�� ������ ��������� ��
					System.out.println(mo.getId()+"���� �������ϴ�.");
					break;
				}
					
			}
			
			if(dis != null) {
				try {
					dis.close();
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
			if(socket != null) {
				try {
					socket.close();
				} catch (Exception e) {
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
				System.out.println("�մ��� �����ϼ̽��ϴ�.");
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
