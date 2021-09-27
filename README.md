# AprendiendoPython-Y-GitHub
Aprendiendo Python al mismo tiempo que Git y GitHub  
Este es un proyecto de prueba en el cual aprendo como se usa Git y GitHub al mismo tiempo que aprendo Python

# Aprendiendo Markdown
## My first steps

<!-- italic -->
this is an *italic* text  

<!-- strong -->
this is an **strong** text  

<!-- strikethrough -->
este es un ~~texto~~ tachado  

<!-- Listas -->
* manzana
	* apple 2
* naranja
* etc

1. apple
	1. eat apple
2. orange
3. etc

<!-- Enlaces -->
[google](https://www.google.com "Se ve cuando se pasa el cursor")  
[firefox](https://www.firefox.com "Navegador Firefox")  

<!-- Citas -->
> this is a quote

<!-- Lineas divisoras -->
---
___

<!-- Pegar codigo(una sola linea) -->
`console.log('Hello word')`

<!-- Pegar codigo(varias lineas) 
	 Para resaltar codigo identificar el lenguaje
-->
```c
void fSeleccion(int A[], int n){
    int p, temp;
    for (int k = 0; k < n-1; ++k){
        p=k;
        for (int i = k+1; i < n; ++i){
            if(A[i]<A[p])
                p=i;
        }
        if (k!=p){
            temp = A[p];
            A[p] = A[k];
            A[k] = temp;
        }
        
        //printf("Iteracion %d\n", k+1);
    }
    return;
}

```

<!-- Creacion de tablas(se crean manualmente)
	 Los dos puntos ":" son para identificar la alineación
-->
| Table			| Are			| Cool 		|
| --------- 	|:---------:	| ---------:|
| col 3 is 		| rigth-aligned	| $1600		|
| col 2 is 		| centered		| $12		|
| zebra stripes	| are neat 		| $1		|


<!-- Imagenes -->
![Visual Studio Code](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.gratistodo.com%2Fwp-content%2Fuploads%2F2017%2F02%2FPlayas-14.jpg&f=1&nofb=1 "Se ve cuando se pasa el cursor")

<!-- GITHUB -->
<!-- TO DO -->
* [x] Hola que hace? 1
* [ ] Hola que hace? 2
* [ ] Hola que hace? 3
* [x] Hola que hace? 4

<!-- EMOJIS Y MENCIONES -->
<!-- Se debe de buscar el tipo de emoji que uno quiera
	 Se menciona a una persona por GitHub -->
@Caiuss24001000 :wolf:
