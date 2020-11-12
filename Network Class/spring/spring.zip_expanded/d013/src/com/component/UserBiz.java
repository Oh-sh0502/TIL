package com.component;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Service;

import com.frame.Biz;
import com.frame.Dao;

@Service("ubiz")
public class UserBiz implements Biz {
	
	@Autowired
	@Qualifier("oracledao")
	Dao dao;
	
	
	/*
	 * @Resource(name="oracledao") Dao dao;
	 */
	
	/*
	 * @Autowired Dao dao;
	 */
	
	/*
	 * public UserBiz() { }
	 * 
	 * public UserBiz(Dao dao) { this.dao = dao; }
	 */
	
	public void setDao(Dao dao) {
		this.dao = dao;
	}
	
	
	@Override
	public void register() {
		dao.insert();
	}

	@Override
	public void remove() {
		dao.delete();
	}

	@Override
	public void modify() {
		dao.update();
	}

}
