package com.controller;

import javax.annotation.Resource;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import com.frame.Biz;
import com.vo.UserVO;

@Controller
public class MainController {
	
	@Resource(name="ubiz")
	Biz<String, UserVO> biz;
	
	@RequestMapping("/s_main.mc")
	public ModelAndView s_main() {
		ModelAndView mv = new ModelAndView();
		mv.setViewName("Searcher/s_main");
		return mv;
	}

	@RequestMapping("/m_main.mc")
	public ModelAndView m_main() {
		ModelAndView mv = new ModelAndView();
		mv.setViewName("Manager/m_main");
		return mv;
	}
	@RequestMapping("/login.mc")
	public ModelAndView login() {
		ModelAndView mv = new ModelAndView();
		mv.setViewName("Searcher/s_login");
		return mv;
	}
	
}
