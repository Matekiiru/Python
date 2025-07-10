cursos, disciplinas, professores = [], [], []
curso = {'id':'','nome':''}
professor = {'id':'','nome':''}
disciplina = {'id':'','nome':'','id_curso':'','id_professor':''}
curso_cod, professor_cod, disciplina_cod = 1, 1, 1
id_curso, id_professor, id_disciplina = 1, 1, 1

opcao_menu = 1
while opcao_menu > 0:
  print('[1] - Cadastrar curso')
  print('[2] - Visualizar curso')
  print('[0] - Sair')
  opcao_menu = int(input('Informe a opção desejada: '))
  while opcao_menu < 0 or opcao_menu > 7:
    print('Opção incorreta !!')
    print()
    print('[1] - Cadastrar curso')
    print('[2] - Visualizar curso')
    print('[0] - Sair')
    opcao_menu = int(input('Informe a opção desejada: '))
  if opcao_menu > 0:
    if opcao_menu == 1:
      print()
      codigo = ''
      if id_curso < 10: #0000 a 9999
        codigo = '000' + str(id_curso) #0009
      elif id_curso >= 10 and id < 100:
        codigo = '00' + str(id_curso) #0099
      elif id_curso >= 100 and id < 1000:
        codigo = '0' + str(id_curso) #0999
      else:
        codigo = str(id_curso) #1000
      curso['id'] = codigo
      nome_curso = input('Informe o nome do curso: ')
      curso['nome'] = nome_curso
      cursos.append(curso.copy())
      curso.clear()
      id_curso += 1
    elif opcao_menu == 2:
      print()
      if cursos == []:
        print('Nenhum curso cadastrado !!')
      else:
        for i in range(len(cursos)):
          print(cursos[i]['nome'])
  print()