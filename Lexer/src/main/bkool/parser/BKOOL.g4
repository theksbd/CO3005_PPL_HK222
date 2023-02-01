grammar BKOOL;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: EOF;

// Use ANTLR to write regular expressions describing a Pascal identifier that must begin with a
// lowercase letter (’a’ to ’z’), but may continue with many characters which are lowercase letter
// or digit (’0’ to ’9’).

// IDENTIFIER: [a-z][a-z0-9]*;

// Use ANTLR to write regular expressions describing Pascal tokens For a number to be taken as
// "real" (or "floating point") format, it must either have a decimal point, or use scientific
// notation. For example, 1.0, 1e-12, 1.0e-12, 0.000000001 are all valid reals. At least one digit
// must exist on either side of a decimal point.

// REAL: INTPART (FRACPART EXPPART? | EXPPART); fragment INTPART: [0-9]+; fragment FRACPART: '.'
// [0-9]+; fragment EXPPART: 'e' '-'? [0-9]+;

// Use ANTLR to write regular expressions describing Pascal strings are made up of a sequence of
// characters between single quotes: 'string'. The single quote itself can appear as two single
// quotes back to back in a string: 'isn''t'.

// STRING: SingQ (~['] | SingQ SingQ)* SingQ; fragment SingQ: '\'';

// Khi nhập học tại trường Đại học Bách Khoa, sinh viên được yêu cầu đặt một tên tài khoản gọi là
// BKNetID, gồm ba thành phần theo thứ tự: tên, họ và chuỗi tự chọn. Giữa tên và họ, sinh viên phải
// đặt một dấu chấm (.). Tên và họ là chuỗi chỉ bao gồm các ký tự chữ thường với độ dài tối thiểu là
// 1. Chuỗi tự chọn là một chuỗi có chiều dài từ 1 đến 5 kí tự bao gồm chữ thường, ký tự số, dấu
// chấm, dấu gạch dưới nhưng không được kết thúc bằng dấu chấm. Ví dụ: duy.tran2903, duy.tran.3_12
// là các chuỗi BKNetID hợp lệ nhưng duy.tran2903. hoặc duy2.tran2903 là BKNetID không hợp lệ. Hãy
// sử dụng ANTLR để viết biểu thức chính quy cho BKNetID nói trên. Sinh viên phải sử dụng fragment
// để nhận trọn điểm.

// BKNETID: NAME DOT NAME STRING; fragment NAME: [a-z][a-z]*; fragment STRING: [a-z0-9_.]+; fragment
// DOT: '.';

// Use ANTLR to write regular expressions describing a valid IPv4 address. It consists of exact 4 strings, whose length is from 1 to 3, of digits (0-9) but not starting with 0 unless the string is 0. The strings are separated by one dot (.). 

// fragment COM: ([0-9] | [1-9][0-9] | [1-9][0-9][0-9]); IPV4: COM '.' COM '.' COM '.' COM;

// Use ANTLR to write regular expressions describing PHP's integers (in decimal) which is a sequence of digits (0-9) starting with a non-zero digit or only a zero. Integer literals may contain underscores (_) between digits, for better readability of literals but these underscores are removed by PHP's scanner.

// INT: [1-9] [0-9]* ('_' [0-9]+)* {self.text = self.text.replace("_","")} | '0';

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;