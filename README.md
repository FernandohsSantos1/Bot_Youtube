# Bot_Youtube

Como alguns sorteios realizados em lives do youtube levam em conta a quantidade de mensagens enviadas, esse
Bot foi criado para enviar mensagens automáticas no chat, através das lib pyautogui e pyperclip.

O programa recebe como parametros de entrada:

 - URL da live;
 - mensagem a ser enviada;
  
** A automatização do mouse através do pyautogui é calculada a partir de resolução da tela, então é necessário ajustes para monitores com resoluções diferentes.

** É possivel descobrir a posição do mouse através do comando pyautogui.position()
