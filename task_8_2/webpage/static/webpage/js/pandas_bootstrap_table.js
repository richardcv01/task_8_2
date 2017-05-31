   var data = JSON.parse(table.getAttribute("data-attrib"));
   var tabl = document.getElementById('table');

   var i = 0;
   alert(data.length);
   for (var i=0; i<data.length; i++) {
       d = data[i]
       newrow = tabl.insertRow();
       newcell = newrow.insertCell(0);
       newcell.innerText = i;
       newcell = newrow.insertCell(1);
       newcell.innerText = d.cryptoCurrency;
       newcell = newrow.insertCell(2);
       newcell.innerText = d.marcet_cap;
       newcell = newrow.insertCell(3);
       newcell.innerText = d.price;
       newcell = newrow.insertCell(4);
       newcell.innerText = d.circulating_supply;
       newcell = newrow.insertCell(5);
       newcell.innerText = d.volum;
       newcell = newrow.insertCell(6);
       newcell.innerText = d.h1;
       newcell = newrow.insertCell(7);
       newcell.innerText = d.h24;
       newcell = newrow.insertCell(8);
       newcell.innerText = d.d7;
       newcell = newrow.insertCell(9);
       newcell.innerText = d.insert_date;
   }





