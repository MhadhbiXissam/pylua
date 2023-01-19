from  astTypes import *
import  astTypes as T
from builtIn import BuiltInLua
__BuiltInLua__ = BuiltInLua()

def Module__repr__(self) :  
	return "\n".join([ repr(trunc) for trunc in self.body ])
Module.__repr__  = Module__repr__
		

def Name__repr__(self) :
	return f"{self.id}"
Name.__repr__  = Name__repr__


def Constant__repr__(self) :
	if isinstance(self.value,bool)  : return repr(self.value).lower()
	if isinstance(self.value,int) or isinstance(self.value,float)  : return repr(self.value)
	if isinstance(self.value,str)  : return json.dumps(self.value)
	if self.value == None : return repr(self.value)
Constant.__repr__  = Constant__repr__




def AnnAssign__repr__(self) :
	return f"{self.annotation} {self.target}" + (f" = {self.value}" if self.value != None else   " = nil" ) 
AnnAssign.__repr__  = AnnAssign__repr__

def Assign__repr__(self) :
	repr_value = None
	if isinstance(self.value,bool)  : repr_value =  repr(self.value).lower()
	if isinstance(self.value,int) or isinstance(self.value,float)  : repr_value =  repr(self.value)
	if isinstance(self.value,str)  : repr_value = json.dumps(self.value)
	if self.value == None : repr_value =  "nil"
	if repr_value == None : repr_value = repr(self.value)
	return f"{self.targets[0]} = {repr_value}"
Assign.__repr__  = Assign__repr__



def Tuple_repr__(self) :
	Tuple(elts=[Constant(value=1, kind=None), Constant(value=2, kind=None)], ctx=Load())
	return f"{' , '.join([repr(e) for e in self.elts])}"
Tuple.__repr__  = Tuple_repr__

def Set_repr__(self) :
	return f"{{{' , '.join([repr(e) for e in self.elts])}}}"
Set.__repr__  = Set_repr__

def Dict_repr__(self) :
	return "{" + ",".join([f"{repr(self.keys[i])} = {repr(self.values[i])}"  for i in range(len(self.keys))]) + "}"
Dict.__repr__  = Dict_repr__

def List_repr__(self) :
	return "["  + f"{repr(self.elts[0])}" + "]"
List.__repr__  = List_repr__

def Pass_repr__(self) :
	return ""
Pass.__repr__  = Pass_repr__

def For_repr__(self) :
	if isinstance(self.target,T.Tuple)  :
		bod = "\n".join([repr(body) for body in self.body])
		return f"for {self.target} in pairs({self.iter}) do\n"  + bod + "\nend "
	else  : 
		bod = "\n".join([repr(body) for body in self.body])
		return f"for {self.target} = {self.iter} do\n"  + bod + "\nend "
For.__repr__  = For_repr__

def If__repr__(self) :
	result = ""
	result = f"if {self.test} then \n" + "\n".join([repr(body) for body in self.body]) 
	if len(self.orelse) > 0  : 
		if   isinstance(self.orelse[0],T.If)  :
			result += f"\nelse{repr(self.orelse[0])}" 
		else  : 
			bod = '\n'.join([repr(body) for body in self.orelse])
			result += f"\nelse \n {bod}"  + "\nend" 
		return result
	else : 
		return result + "\nend"
If.__repr__  = If__repr__

def GtE__repr__(self) :
	return ">="
GtE.__repr__  = GtE__repr__

def LtE__repr__(self) :
	return "<="
LtE.__repr__  = LtE__repr__

def Gt__repr__(self) :
	return ">"
Gt.__repr__  = Gt__repr__

def Lt__repr__(self) :
	return "<"
Lt.__repr__  = Lt__repr__


def Compare__repr__(self) :
	if len(self.ops) == 1  : 
		return f"({self.left} {' '.join([repr(op) for op in self.ops])} {' '.join([repr(comp) for comp in self.comparators])})"
	if len(self.ops) == 2  : 
		return "( " + f"({self.left} {repr(self.ops[0])} {repr(self.comparators[0])})" + " and " +  f"( {repr(self.comparators[0])} {repr(self.ops[1])} {repr(self.comparators[1])}  ) )"
Compare.__repr__  = Compare__repr__



def BoolOp__repr__(self) :
	return "( " + f" {self.op} ".join([repr(val) for val in self.values]) + " )"
BoolOp.__repr__  = BoolOp__repr__

def And__repr__(self) :
	return f"and"
And.__repr__  = And__repr__

def Or__repr__(self) :
	return f"or"
Or.__repr__  = Or__repr__

def Not__repr__(self) :
	return f"not"
Not.__repr__  = Not__repr__


def UnaryOp__repr__(self) :
	return f"{self.op}{self.operand}"
UnaryOp.__repr__  = UnaryOp__repr__


def Eq__repr__(self) :
	return "=="
Eq.__repr__  = Eq__repr__

def NotEq__repr__(self) :
	return "~="
NotEq.__repr__  = NotEq__repr__

def Add__repr__(self) :
	return "+"
Add.__repr__  = Add__repr__

def Mult__repr__(self) :
	return "*"
Mult.__repr__  = Mult__repr__

def Sub__repr__(self) :
	return "-"
Sub.__repr__  = Sub__repr__

def Div__repr__(self) :
	return "/"
Div.__repr__  = Div__repr__

def AugAssign__repr__(self) :
	return f"{self.target} = {self.target} {self.op} ({self.value})"
AugAssign.__repr__  = AugAssign__repr__


def BinOp__repr__(self) :
	return f"({self.left} {self.op} {self.right})"
BinOp.__repr__  = BinOp__repr__


def arg__repr__(self) :
	return f"{self.arg}"
arg.__repr__  = arg__repr__

def Return__repr__(self) :
	return f"return {self.value}"
Return.__repr__  = Return__repr__

def arguments__repr__(self) :
	return ",".join([repr(arg) for arg in self.args])
arguments.__repr__  = arguments__repr__

def FunctionDef__repr__(self) :
	if self.returns == None :
		result = f"function {self.name}({self.args})\n" + "\n".join([repr(b) for b in self.body]) + "\nend"
		return result
	if self.returns.id == "local" :
		result = f"local function {self.name}({self.args})\n" + "\n".join([repr(b) for b in self.body]) + "\nend"
		return result

	if self.returns.id == "lvar" :
		result = f"local {self.name} = function ({self.args})\n" + "\n".join([repr(b) for b in self.body]) + "\nend"
		return result

	if self.returns.id == "gvar" :
		result = f"{self.name} = function ({self.args})\n" + "\n".join([repr(b) for b in self.body]) + "\nend"
		return result
FunctionDef.__repr__  = FunctionDef__repr__

def Call__repr__(self) :
	func = None
	if isinstance(self.func,T.Name) : 
		func = __BuiltInLua__.get_func(self.func.id)
	if func == None : 
		result = f"{self.func}(" + ",".join([repr(b) for b in self.args]) + ")"
		return result
	else :
		result = BuiltInLua.__dict__[func](self.args , self.keywords)
		return result
Call.__repr__  = Call__repr__


def Expr__repr__(self) :
	result = f"{self.value}"
	return result
Expr.__repr__  = Expr__repr__


def Attribute__repr__(self) :
	result = f"{self.value}.{self.attr}"
	return result
Attribute.__repr__  = Attribute__repr__



def Index__repr__(self) :
	result = f"{self.value}"
	return result
Index.__repr__  = Index__repr__

def Subscript__repr__(self) :
	result = f"{self.value}[{self.slice}]"
	return result
Subscript.__repr__  = Subscript__repr__

def Import__repr__(self) :
	result = ""
	assert(len(self.names) == 1 )
	if self.names[0].asname == None :
		return f"require \"{self.names[0].name}\""
	else : 
		return f"local {self.names[0].asname}  = require(\"{self.names[0].name}\")"
	return result
Import.__repr__  = Import__repr__



def IfExp__repr__(self) :
	return f"(({self.test}) and {self.body} or  {self.orelse} )"
IfExp.__repr__  = IfExp__repr__

def keyword__repr__(self) :
	return f"{self.arg} = {self.value}"
keyword.__repr__  = keyword__repr__

def USub__repr__(self) :
	return "-"
USub.__repr__  = USub__repr__

def Assert__repr__(self) :
	return f"assert({self.test}" + ")" if self.msg == None else ",{self.msg})"
Assert.__repr__  = Assert__repr__


ast_globals = {
'Module' : Module,
'Name' : Name,
'Constant' : Constant,
'AnnAssign' : AnnAssign,
'Assign' : Assign,
'Tuple' : Tuple,
'Set' : Set,
'Dict' : Dict,
'List' : List,
'Pass' : Pass,
'For' : For,
'If' : If,
'GtE' : GtE,
'LtE' : LtE,
'Gt' : Gt,
'Lt' : Lt,
'Compare' : Compare,
'BoolOp' : BoolOp,
'And' : And,
'Or' : Or,
'Not' : Not,
'UnaryOp' : UnaryOp,
'Eq' : Eq,
'NotEq' : NotEq,
'Add' : Add,
'Mult' : Mult,
'Sub' : Sub,
'AugAssign' : AugAssign,
'BinOp' : BinOp,
'arg' : arg,
'Return' : Return,
'arguments' : arguments,
'FunctionDef' : FunctionDef,
'BuiltInLua' : BuiltInLua,
'Call' : Call,
'Expr' : Expr,
'Attribute' : Attribute,
'Index' : Index,
'Subscript' : Subscript,
'Import' : Import,
'IfExp' : IfExp,
'keyword' : keyword , 
"Store" : Store,
"Load" : Load , 
"alias" : alias , 
"USub" : USub , 
"Div" : Div , 
"Assert" : Assert
}
