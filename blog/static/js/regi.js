$('input').focus(function(){
  if($(this).attr('placeholder')&& $(this).val()!=""){
    $('.ph').fadeOut();
    $(this).after('<div class="ph">'+$(this).attr('placeholder')+'</div>');
    $(this).parent().find('.ph').fadeIn();
  }
});
$('input').keyup(function(){
  console.log($(this).val());
  if($(this).attr('placeholder')&&$(this).val!=""){
    $(this).after('<div class="ph">'+$(this).attr('placeholder')+'</div>');
    $(this).parent().find('.ph').fadeIn();
  }
});
$('input').blur(function(){
     $('.ph').fadeOut();
});
