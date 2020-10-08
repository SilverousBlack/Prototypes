"""
Prototype Algorithms Core - Tree Library
(c) Silverous Black, 2020

License(s): MIT Licence

Notice: The distribution, ownership, reproduction and use of this library is subject to the above stated license.

Python Tree
    PyTree Model 1
    Complex Data Storage/Mapping
    CDSM-T001P

----- ----- ----- ----- -----
Object: TreeNode
Members:
    > __uid (variable) - tree node unique ID
    > __val (variable) - data stored in node
    > __pn (vairable) - represents parent node nature of the node
    > __nodes (variable) - memory space containing child nodes
    > set_uid (function) - sets the UID of the node
    > set_value (function) - sets the value of the node
    > attach_node (function) - attaches a sub node into the node
----- ----- ----- ----- -----

"""
from Core_Utilities import CDSM

class TreeNode(CDSM):
    __uid: int
    __pn: bool
    __nodes: list
    
    def __verify_nodes(self):
        for i in self.__nodes:
            if not isinstance(i, TreeNode):
                raise ValueError
        
    def __get(self, index: list):
        h = index.pop(0)
        if not isinstance(h, (int, slice)):
            raise IndexError
        elif len(index) > 0:
            return self.__nodes[h].__get(index)
        else:
            return self.__nodes[h]
    
    def __set(self, index: list, value):
        h = index.pop()
        if not isinstance(h, int):
            raise IndexError
        elif len(index) > 0:
            self.__nodes[h].__set(index, value)
        else:
            self.__nodes[h] = value
            
    def __del(self, index: list):
        h = index.pop()
        if not isinstance(h, (int, slice)):
            raise IndexError
        elif len(index) > 0:
            self.__nodes[h].__del(index)
        else:
            del self.__nodes[h]
    
    def __init__(self, otuid = None, value = None, nodes: list = []):
        if isinstance(otuid, TreeNode):
            self.__uid = int(otuid.__uid)
            self.__val = otuid.__val.__class__(otuid.__val)
            self.__pn = bool(otuid.__pn)
            self.__nodes = [] if self.__pn == False else list(otuid.__nodes)
            self.__verify_nodes()
        else:
            self.__uid = int(otuid)
            self.__val = value.__class__(value)
            self.__nodes = list(nodes)
            self.__pn = True if len(self.__nodes) > 0 else False
            self.__verify_nodes()
            
    def __repr__(self):
        return ("TreeNode <%s> : %s : " % (self.__uid, self.__val)) + (repr(self.__nodes) if self.__pn == True else "<no nodes>")
    
    def __len__(self):
        return len(self.__nodes)
    
    def __getitem__(self, index):
        if isinstance(index, (int, slice)):
            return (self.__nodes[index])
        elif isinstance(index, list):
            return self.__get(index)
        
    def __setitem__(self, index, value):
        if isinstance(index, (int, list)):
            if not isinstance(value, TreeNode):
                raise ValueError
            elif isinstance(index, int):
                self.__nodes[index] = value
            else:
                self.__set(index, value)
    
    def __delitem__(self, index):
        if isinstance(index, int):
            del self.__nodes[index]
        elif isinstance(index, slice):
            del self.__nodes[index]
        elif isinstance(index, list):
            self.__del(index)
            
    def set_uid(self, uid: int):
        self.__uid = uid
        return self
    
    def set_value(self, value):
        del self.__val
        self.__val = value.__class__(value)
        
    def attach_node(self, nodes):
        if isinstance(nodes, list):
            self.__pn = True
            for i in nodes:
                if not isinstance(i, TreeNode):
                    raise ValueError
                else:
                    self.__nodes.append(i)
        elif isinstance (nodes, TreeNode):
            self.__pn = True
            self.__nodes.append(nodes)
        else:
            raise ValueError
        return self

class Tree(CDSM):
    __root: TreeNode
    __count: int
    
    
    def __do_uid(self, loc: list):
        self.__root[loc].set_uid(self.count)
    
    def __fix_init_uid(self):
        loc = []
        self.__root.set_uid(self.__count)
        self.__count += 1
        if len(self.__root) > 0:
            loc.append(0)
            
        
    
    def __init__(self, other):
        self.__count = 0
        if not isinstance(other, (Tree, TreeNode)):
            raise ValueError
        else:
            self.__root = TreeNode(other) if isinstance(other, TreeNode) else TreeNode(other.__root)
        self.__fix_init_uid()
