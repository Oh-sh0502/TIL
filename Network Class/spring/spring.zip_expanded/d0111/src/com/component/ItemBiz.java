package com.component;

import org.springframework.stereotype.Component;

import com.biz.Biz;
@Component("ibiz")
public class ItemBiz implements Biz {

	public ItemBiz() {
		System.out.println("ItemBiz constructor ");
	}
	
	@Override
	public void register() {
		System.out.println("Item register");
	}

	@Override
	public void remove() {
		System.out.println("Item remove");

	}

	@Override
	public void modify() {
		System.out.println("Item modify");

	}

}
