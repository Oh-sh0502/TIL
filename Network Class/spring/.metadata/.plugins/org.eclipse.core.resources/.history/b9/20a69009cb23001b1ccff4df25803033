<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<script src="http://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.js"></script>


</head>
<body>
	<input type="button" id="enterBtn" value="ENTER">
	<input type="button" id="exitBtn" value="EXIT">
	<p>
		session ID : <input type="text" id="sessionid" value="" size="50"/>
	</p>
	<input type="text" id="message" value="50">
	<input type="button" id="sendBtn" value="SEND">
	
	<div id="data"></div>
</body>
<script type="text/javascript">
	var ws;
	$(document).ready(function(){
		
		$("#enterBtn").click(function(){
			ws = new WebSocket("ws://192.168.0.17/websocket_bean/ws");
			ws.onerror = onError;
			wd.onmessage = onMessage;
			ws.onopen = onOpen;
			ws.onclose = onclose;	
		});
	
		$("#exitBtn").click(function(){
			ws.close();
		});
		
		$("#sendBtn").click(function(){
			sendMessage();
		});
	});
	
	function sendMessage(){
		ws.send($('#message').val());
	}
	
	function onMessage(event){
		var data = event.data;
		$('#data').append(data + "<br>");
	}
	
	function onOpen(event){
		$('#data').append("클라이언트측 onOpen() : Connection Opened!<br>");
	}
	
	function onClose(event){
		$('#data').append("클라이언트측 onClose() : Connection Closed!<br>");
	}
	
	function onError(event){
		$('#data').append("클라이언트측 onError() : Connection Error!<br>");
	}
	
	



</script>
</html>