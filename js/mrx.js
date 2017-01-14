var user = { 
    _name: 'mr x', 
    id: function (){ 
        return this._name; 
    } 
}; 

var copy = user.id.bind(user); 
 
console.log(copy());
console.log(user.id());