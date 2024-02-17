from language.resolvers.AddFunctionResolver import AddFunctionResolver
from language.resolvers.AddSubResolver import AddSubResolver
from language.resolvers.ArithmeticNodeResolver import ArithmeticNodeResolver
from language.resolvers.AssignStatResolver import AssignStateResolver
from language.resolvers.BooleanArithmeticResolver import BooleanArithmeticResolver
from language.resolvers.DefStatResolver import DefStatResolver
from language.resolvers.ElseStatResolver import ElseStatResolver
from language.resolvers.ForEachStatResolver import ForEachStatResolver
from language.resolvers.ForStatResolver import ForStatResolver
from language.resolvers.GetFunctionResolver import GetFunctionResolver
from language.resolvers.IfStatResolver import IfStatResolver
from language.resolvers.ListNodeResolver import ListNodeResolver
from language.resolvers.LogicalResolver import LogicalResolver
from language.resolvers.MulDivResolver import MulDivResolver
from language.resolvers.NodeReferenceResolver import NodeReferenceResolver
from language.resolvers.NodeResolver import NodeResolver
from language.resolvers.ObjectNodeResolver import ObjectNodeResolver
from language.resolvers.ParenArithmeticNodeResolver import ParenArithmeticNodeResolver
from language.resolvers.ParenBooleanNodeResolver import ParenBooleanNodeResolver
from language.resolvers.ProgResolver import ProgResolver
from language.resolvers.RelationalResolver import RelationalResolver
from language.resolvers.ReturnStatResolver import ReturnStatResolver
from language.resolvers.StatResolver import StatResolver
from language.resolvers.UnaryArithmeticResolver import UnaryArithmeticResolver
from language.resolvers.VariableResolver import VariableResolver
from language.resolvers.WithPredicateResolver import WithPredicateResolver


class Initializer:

    def __init__(self):
        ProgResolver()
        StatResolver()
        ReturnStatResolver()
        BooleanArithmeticResolver()
        ArithmeticNodeResolver()
        UnaryArithmeticResolver()
        AddSubResolver()
        MulDivResolver()
        RelationalResolver()
        LogicalResolver()
        NodeResolver()
        DefStatResolver()
        VariableResolver()
        NodeReferenceResolver()
        WithPredicateResolver()
        AssignStateResolver()
        IfStatResolver()
        ElseStatResolver()
        ForEachStatResolver()
        ForStatResolver()
        GetFunctionResolver()
        ObjectNodeResolver()
        ListNodeResolver()
        AddFunctionResolver()
        ParenArithmeticNodeResolver()
        ParenBooleanNodeResolver()