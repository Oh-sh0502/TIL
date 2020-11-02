package com.tcpip;

import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.util.Scanner;

public class Client {
	// 클라이언트가 서버에 접속하기 위해 필요한 멤버변수
	int port;
	String address;
	Socket socket;
	// 기본생성자
	public Client() {}
	
	// 주소와 포트를 받는 생성자
	public Client(String address,int port) {
		this.address = address;
		this.port = port;
	}
	
	// 접속 시도 함수(소켓 생성)
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
	
	// 보내기 쓰레드 정의 (아웃풋스트림)
	class Sender extends Thread{
		DataOutputStream dos;
		String msg;
		public Sender(String msg) {
			this.msg = msg;
			try {
				dos = new DataOutputStream(socket.getOutputStream());
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
		@Override
		public void run() {
			if(dos !=null) {
				try {
					dos.writeUTF(msg);		// 보내기
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
		}
		
	}
	
	// 서버로 메시지를 전달해주는 함수
	public void request() throws IOException {
		// 보낼 메세지 입력
		Scanner sc = new Scanner(System.in);
		try {
			// 계속해서 여러 메세지를 전달할 수 있게 와일
			while(true) {
				System.out.println("Input Msg .."); 
				String msg = sc.nextLine();
				// q를 입력하면 종료
				if(msg.contentEquals("q")) {
					new Sender("q").start();
					Thread.sleep(1000);
					System.out.println("Exit Client .. ");
					break;
				}
				new Sender(msg).start();
			}
		}catch(Exception e){
			
		}finally {
			sc.close();			// q를 눌렀다면 소켓을 바로 꺼버림
			if(socket != null) {
				socket.close();
			}
		}
	}
	public static void main(String[] args) {
		Client client = new Client("192.168.0.21", 7777);
		try {
			client.connect();	// 접속을 시도합니다.
			client.request();	// 메시지 전송을 요청합니다.
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

}
