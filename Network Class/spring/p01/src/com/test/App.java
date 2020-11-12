package com.test;

import java.util.ArrayList;

import org.springframework.context.support.AbstractApplicationContext;
import org.springframework.context.support.GenericXmlApplicationContext;

import com.frame.Biz;
import com.vo.UserVO;

public class App {

	public static void main(String[] args) {
		System.out.println("App Start ....");
		AbstractApplicationContext factory =
				new GenericXmlApplicationContext("myspring.xml");
		System.out.println("Sping Started ....");
		
		Biz<String,UserVO> biz = 
				(Biz)factory.getBean("ubiz");
	
	
	// Register System
//		UserVO u = new UserVO("oh34sung", "pwd02", "ȫ�浿");
//			try {
//				biz.register(u);
//				System.out.println("OK");
//			} catch (Exception e) {
//				e.printStackTrace();
//			}
		
	// Select System
//		UserVO content = null;
//		try {
//			content = biz.get("oh34sung");
//			System.out.println(content);
//		} catch (Exception e) {
//			e.printStackTrace();
//		}
		
	// SelectAll System
		ArrayList<UserVO> list = null;
			try {
				list = biz.get();
				for(UserVO co:list) {
					System.out.println(list);
				}
			} catch (Exception e) {
				e.printStackTrace();
			}

	
			factory.close();
			System.out.println("Spring End ....");
			System.out.println("App End ....");
}
}
