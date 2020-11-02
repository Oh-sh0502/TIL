package com.tcpip2;

import java.io.DataOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.net.Socket;
import java.util.Scanner;

import com.msg.Msg;

public class Client {
	// Ŭ���̾�Ʈ�� ������ �����ϱ� ���� �ʿ��� �������
	int port;
	String address;
	Socket socket;
	// �⺻������
	public Client() {}
	
	// �ּҿ� ��Ʈ�� �޴� ������
	public Client(String address,int port) {
		this.address = address;
		this.port = port;
	}
	
	// ���� �õ� �Լ�(���� ����)
	public void connect() throws Exception {
		try {
			socket = new Socket(address,port);
			System.out.println("Connected ...");
		} catch (Exception e) {
			while(true) {
				Thread.sleep(2000);
				try {
					socket = new Socket(address,port);
					System.out.println("Connected ...");
					break;
				} catch (Exception e1) {
					System.out.println("Retry ...");
				}
			}
		}
	} 
	
	// ������ ������ ���� (�ƿ�ǲ��Ʈ��)
	class Sender extends Thread{
		// object�� ��Ʈ������ ���� ���� ObjectOutputStream
		ObjectOutputStream dos;
		Msg mo;
		public Sender(Msg mo) {
			this.mo = mo;
			try {
				dos = new ObjectOutputStream(socket.getOutputStream());
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
		@Override
		public void run() {
			if(dos !=null) {
				try {
					dos.writeObject(mo);		// ������( object�� ���� ���� writeObject())
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
		}
		
	}
	
	// ������ �޽����� �������ִ� �Լ�
	public void request() throws IOException {
		// ���� �޼��� �Է�
		Scanner sc = new Scanner(System.in);
		try {
			// ����ؼ� ���� �޼����� ������ �� �ְ� ����
			while(true) {
				System.out.println("Input Msg .."); 
				String msg = sc.nextLine();
				Msg mo = new Msg("192.168.0.21","[tiger]",msg.trim());
				// q�� �Է��ϸ� ����
				if(msg.contentEquals("q")) {
					new Sender(mo).start();
					Thread.sleep(1000);
					System.out.println("Exit Client .. ");
					break;
				}
				new Sender(mo).start();
				System.out.println(mo.getIp()+mo.getId()+mo.getMsg());
			}
		}catch(Exception e){
			
		}finally {
			sc.close();			// q�� �����ٸ� ������ �ٷ� ������
			if(socket != null) {
				socket.close();
			}
		}
	}
	public static void main(String[] args) {
		Client client = new Client("192.168.0.21", 7777);
		try {
			client.connect();	// ������ �õ��մϴ�.
			client.request();	// �޽��� ������ ��û�մϴ�.
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

}
