from .query_starter import query_starter
from .prompt_invoker import prompt_invoker
from .llm_invoker import llm_invoker
from .parser import parser
from .executer import executer
from .query_ender import query_ender


chain1234 = query_starter | prompt_invoker | llm_invoker | parser
chain52346 = executer | prompt_invoker | llm_invoker | parser | query_ender
chain6 = query_ender
