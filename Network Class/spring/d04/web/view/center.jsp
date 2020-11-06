<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>    
<script>
$(document).ready(function(){
	$('button').click(function(){
		var sid = $('input[name="id"]').val();
		$.ajax({
			url:'get.mc',
			data:{'id':sid},
			success:function(data){
				alert('|'+data+'|');
			}
		});
	});
});

</script>    
    
    
<div id="center">
<h1>Main Center Page</h1>
<button>Click</button>
<input type="text" name="id">
</div>









