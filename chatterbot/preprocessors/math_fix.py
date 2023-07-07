def fix_math(statement):
 statement.text=statement.text.replace('+',' + ')
 statement.text=statement.text.replace('-',' - ')
 statement.text=statement.text.replace('/',' / ')
 statement.text=statement.text.replace('*',' * ')
 statement.text=statement.text.replace('%',' % ')
 statement.text=statement.text.replace('^',' ^ ')
 return statement
