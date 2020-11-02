package com.tcpip2;

import java.io.IOException;
import java.io.ObjectInputStream;
import java.net.ServerSocket;
import java.net.Socket;

import com.msg.Msg;

// Object Serialization

public class Server {

	int port;
	// 멤버 변수
	ServerSocket serverSocket;
	Socket socket;
	
	
	// 기본 생성자
	public Server() {}
	
	// 포트를 받는 생성자
	public Server(int port) {
		this.port = port;
	}
	
	// 클라이언트의 소켓을 받는 쓰레드 정의(클라이언트와 파이프라인 구축: 인풋스트림)
	class Receiver extends Thread{
		// object 받을 때는 ObjectInputStream
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
		
		// 받아와서 처리
		@Override
		public void run() {
			while(dis != null) {
				Msg mo = null;
				// object 객체 선언
				try {
					// object를 받을 때는 이렇게!
					mo = (Msg) dis.readObject();
					System.out.println(mo.getId()+mo.getIp()+mo.getMsg());
					dis = new ObjectInputStream(socket.getInputStream());
					if(mo.getMsg().equals("q")) {
						System.out.println(mo.getId()+"님이 나갔습니다.");
						break;
					}
					System.out.println(mo.getId()+":"+mo.getMsg());
				} catch (Exception e) {
					// 클라이언트가 연결을 끊어버렸을 시
					System.out.println(mo.getId()+"님이 나갔습니다.");
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
	
	// 서버 시작 함수. 서버가 시작하면 서버 소켓이 만들어지면서 어셉트로 기다리고 누군가가 들어오면 소켓을 생성한다.
	public void startServer() throws Exception {
		System.out.println("TCP/IP Server Start ...");
		// Exception 이 일어났을 때 대처할 수 있는 구조
		try {
			serverSocket = new ServerSocket(port);
			// 서버는 언제든지 죽지않고 살아있어야 하므로 와일
			while(true) {
				System.out.println("Ready Server ..");
				// 클라이언트를 받게 되면서 소켓이 생김.
				socket = serverSocket.accept();
				// 클라이언트가 드러오면 연결되었다고 출력
				System.out.println("손님이 입장하셨습니다.");
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
