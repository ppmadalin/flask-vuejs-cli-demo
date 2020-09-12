(function(t){function e(e){for(var n,i,d=e[0],s=e[1],c=e[2],u=0,f=[];u<d.length;u++)i=d[u],Object.prototype.hasOwnProperty.call(r,i)&&r[i]&&f.push(r[i][0]),r[i]=0;for(n in s)Object.prototype.hasOwnProperty.call(s,n)&&(t[n]=s[n]);l&&l(e);while(f.length)f.shift()();return a.push.apply(a,c||[]),o()}function o(){for(var t,e=0;e<a.length;e++){for(var o=a[e],n=!0,d=1;d<o.length;d++){var s=o[d];0!==r[s]&&(n=!1)}n&&(a.splice(e--,1),t=i(i.s=o[0]))}return t}var n={},r={app:0},a=[];function i(e){if(n[e])return n[e].exports;var o=n[e]={i:e,l:!1,exports:{}};return t[e].call(o.exports,o,o.exports,i),o.l=!0,o.exports}i.m=t,i.c=n,i.d=function(t,e,o){i.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:o})},i.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},i.t=function(t,e){if(1&e&&(t=i(t)),8&e)return t;if(4&e&&"object"===typeof t&&t&&t.__esModule)return t;var o=Object.create(null);if(i.r(o),Object.defineProperty(o,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var n in t)i.d(o,n,function(e){return t[e]}.bind(null,n));return o},i.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return i.d(e,"a",e),e},i.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},i.p="/";var d=window["webpackJsonp"]=window["webpackJsonp"]||[],s=d.push.bind(d);d.push=e,d=d.slice();for(var c=0;c<d.length;c++)e(d[c]);var l=s;a.push([0,"chunk-vendors"]),o()})({0:function(t,e,o){t.exports=o("56d7")},"034f":function(t,e,o){"use strict";var n=o("85ec"),r=o.n(n);r.a},"21dc":function(t,e,o){},"45d7":function(t,e,o){"use strict";var n=o("a623"),r=o.n(n);r.a},"56d7":function(t,e,o){"use strict";o.r(e);o("e260"),o("e6cf"),o("cca6"),o("a79d");var n=o("2b0e"),r=function(){var t=this,e=t.$createElement,o=t._self._c||e;return o("div",{attrs:{id:"app"}},[o("Navigation"),o("AddTodo",{on:{"add-todo":t.addTodo}}),o("Todos",{attrs:{todos:t.todos},on:{"del-todo":t.deleteTodo}})],1)},a=[],i=(o("99af"),o("4de4"),o("2909")),d=function(){var t=this,e=t.$createElement;t._self._c;return t._m(0)},s=[function(){var t=this,e=t.$createElement,o=t._self._c||e;return o("nav",{attrs:{id:"navbar"}},[o("div",{staticClass:"navbar__inner"},[o("h1",{staticClass:"navbar__inner__logo"},[t._v("ToDo")]),o("ul",{staticClass:"navbar__inner__menu"},[o("li",[o("a",{attrs:{href:"#"}},[t._v("Home")])]),o("li",[o("a",{attrs:{href:"#"}},[t._v("About")])]),o("li",[o("a",{attrs:{href:"#"}},[t._v("Contact")])])])])])}],c={name:"Navigation"},l=c,u=(o("b3c0"),o("2877")),f=Object(u["a"])(l,d,s,!1,null,"f8384cc8",null),p=f.exports,v=function(){var t=this,e=t.$createElement,o=t._self._c||e;return o("div",[o("div",{staticClass:"container"},[o("form",{on:{submit:t.addTodo}},[o("input",{directives:[{name:"model",rawName:"v-model",value:t.title,expression:"title"}],attrs:{type:"text",name:"title",placeholder:"Add Todo..."},domProps:{value:t.title},on:{input:function(e){e.target.composing||(t.title=e.target.value)}}}),o("input",{staticClass:"btn",attrs:{type:"submit",value:"Add"}})])])])},m=[],h={name:"AddTodo",data:function(){return{title:""}},methods:{addTodo:function(t){t.preventDefault();var e={title:this.title,completed:!1};this.$emit("add-todo",e),this.title=""}}},b=h,_=(o("45d7"),Object(u["a"])(b,v,m,!1,null,"7a1a9ab2",null)),y=_.exports,g=function(){var t=this,e=t.$createElement,o=t._self._c||e;return o("div",{attrs:{id:"todos"}},[o("div",{attrs:{id:"todo-item"}},t._l(t.todos,(function(e){return o("div",{key:e.id,staticClass:"item"},[o("TodoItem",{attrs:{todo:e},on:{"del-todo":function(o){return t.$emit("del-todo",e.id)}}})],1)})),0)])},T=[],O=function(){var t=this,e=t.$createElement,o=t._self._c||e;return o("div",{staticClass:"todo-item",class:{"is-completed":t.todo.completed}},[o("p",[o("input",{attrs:{type:"checkbox"},on:{change:t.markComplete}}),t._v(" "+t._s(t.todo.title)+" "),o("button",{staticClass:"del",on:{click:function(e){return t.$emit("del-todo",t.todo.id)}}},[t._v("x")])])])},j=[],x={name:"TodoItem",props:["todo"],methods:{markComplete:function(){this.todo.completed=!this.todo.completed}}},w=x,C=(o("f445"),Object(u["a"])(w,O,j,!1,null,"a0b5e58a",null)),k=C.exports,$={name:"Todos",components:{TodoItem:k},props:["todos"]},P=$,A=(o("6948"),Object(u["a"])(P,g,T,!1,null,"113100df",null)),E=A.exports,M={name:"App",components:{Navigation:p,AddTodo:y,Todos:E},data:function(){return{todos:[{id:1,title:"My first task",completed:!1},{id:2,title:"My second task",completed:!0}]}},methods:{deleteTodo:function(t){this.todos=this.todos.filter((function(e){return e.id!==t}))},addTodo:function(t){this.todos=[].concat(Object(i["a"])(this.todos),[t])}}},S=M,N=(o("034f"),Object(u["a"])(S,r,a,!1,null,null,null)),I=N.exports;n["a"].config.productionTip=!1,new n["a"]({render:function(t){return t(I)}}).$mount("#app")},6948:function(t,e,o){"use strict";var n=o("f650"),r=o.n(n);r.a},"6de5":function(t,e,o){},"85ec":function(t,e,o){},a623:function(t,e,o){},b3c0:function(t,e,o){"use strict";var n=o("6de5"),r=o.n(n);r.a},f445:function(t,e,o){"use strict";var n=o("21dc"),r=o.n(n);r.a},f650:function(t,e,o){}});
//# sourceMappingURL=app.7b289a96.js.map