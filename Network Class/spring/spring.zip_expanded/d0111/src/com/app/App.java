package com.app;

import org.springframework.context.support.AbstractApplicationContext;
import org.springframework.context.support.GenericXmlApplicationContext;

import com.biz.Biz;

public class App {

	public static void main(String[] args) {
		System.out.println("App Start ....");
		AbstractApplicationContext factory =
		new GenericXmlApplicationContext("com.xml");
		System.out.println("Spring Started ....");
		
		Biz biz = (Biz)factory.getBean("ubiz");
		Biz biz2 = (Biz)factory.getBean("ibiz");
		biz.register();
		biz.modify();
		biz2.register();
		
		factory.close();
		System.out.println("Spring End ....");
		System.out.println("App End ....");
	}

}


/* 
	1. ctx�� �Ľ��� ���� AbstractApplicationContext�� �̿��ϰ� 
  		xml������ ���� ���� GenericXmlApplicationContext�� �̿��ϴ� ���� �ϰ� ������ �Ѿ�� �ȴ�.
	
	2. ApplicationContext�� ����� xml�� ������ bean�� ��� '�ϴ�' '����'�ȴ�.
		���� myspring.xml���� 'UserBiz'Ŭ������ ������ bean�� ubiz�� ibiz�� �ִ�.
		�ϴ� �����س��� getBean���� �������� �����.
*/