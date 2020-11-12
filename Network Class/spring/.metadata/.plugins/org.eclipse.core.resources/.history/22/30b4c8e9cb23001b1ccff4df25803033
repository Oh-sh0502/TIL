package com.controller;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

import org.aspectj.bridge.Message;
import org.springframework.stereotype.Repository;
import org.springframework.web.socket.CloseStatus;
import org.springframework.web.socket.TextMessage;
import org.springframework.web.socket.WebSocketSession;
import org.springframework.web.socket.handler.TextWebSocketHandler;

@Repository
public class MyWebSocketHandler extends TextWebSocketHandler{
	
	private Map<String, WebSocketSession> sessions = new HashMap<String, WebSocketSession>();
	
	// 웹소켓 서버에 클라이언트가 접속하면 호출되는 메소드
	@Override
    public void afterConnectionEstablished(WebSocketSession session) throws Exception {
		System.out.println("세션아이디[" + session.getId() + "] 입장.");
		
		Iterator<String> sessionIds = sessions.keySet().iterator();
		
		String sessionId = "";
		while(sessionIds.hasNext()) {
			sessionId = sessionIds.next();
			sessions.get(sessionId).sendMessage(new TextMessage("[" + session.getId() + "] 입장."));
		}
    }
	
	// 클라이언트가 접속을 종료하면 호출되는 메소드
    @Override
    public void afterConnectionClosed(WebSocketSession session, CloseStatus status) throws Exception {
    	System.out.println("세션아이디[" + session.getId() + "] 퇴장.");
    	
    	sessions.remove(session.getId());
    	Iterator<String> sessionIds = sessions.keySet().iterator();
    	String sessionId = "";
    	while(sessionIds.hasNext()) {
    		sessionId = sessionIds.next();
    		sessions.get(sessionId).sendMessage(new TextMessage("[" + session.getId() + "] 퇴장."));
    	}
    }
 
    // 메시지 전송시나 접속해제시 오류가 발생할 때 호출되는 메소드
    @Override
    public void handleTextMessage(WebSocketSession session, TextMessage message) throws Exception {
    	System.out.println(session.getId() + "이(가) 메세지전송.");
    	Iterator<String> sessionIds = sessions.keySet().iterator();
    	String sessionId = "";
    	while(sessionIds.hasNext()) {
    		sessionId = sessionIds.next();
    		sessions.get(sessionId).sendMessage(new TextMessage(session.getId() + " : " + message.getPayload()));
    	}
    }
	
	
	

}
