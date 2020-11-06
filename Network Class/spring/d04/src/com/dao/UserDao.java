package com.dao;

import org.springframework.stereotype.Repository;

import com.frame.Dao;
import com.vo.UserVO;
@Repository("udao")
public interface UserDao extends Dao<String, UserVO> {
	public int test(String v) throws Exception;
}
