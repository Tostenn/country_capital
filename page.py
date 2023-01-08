

def page(data,name):
    html = '''<!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>T_xOx_T</title>
        <style>
            *{ margin: 0;padding: 0;text-decoration: none;}
            header {
                width: 100%;
                height: 110px;
                padding-top: 15px;
                position: fixed;
                background-color: rgb(255, 252, 252);
            }
            header .tt{

                font-weight: bold;
                font-size: 25px;
                text-align: center;
                font-family: Gill Sans, sans-serif;
            }
            .esp{height: 120px; }
            nav{
                margin-top: 20px;
                width: 100%;
                height: 50px;
                text-align: center;
            }
            .logo, form, .aide{
                display: inline-block;
            }
            .logo{
                font-weight: bold;
                float: left;
                font-size: 25px;
                font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
                margin-left: 10px;
            }
            form{
                /* width: 70%; */
                text-align: center;
                display: inline-block;
                /* padding-left: 30px; */
            }
            #rech{
                width: 110;
                height: 30px;
                text-align: center;
                outline: none;
            }
            input[type="submit"]{
                font-size: 15px;
                font-weight: bold;
                padding: 9px;
                background-color: rgba(10, 199, 233, 0.651);
                border: 0;
                border-radius: 5px;
            }
            .aide{
                font-size: 15px;
                text-transform: capitalize;
                font-weight: bold;
                padding: 4px;
                border-radius: 5px;
                color: black;
                background-color: rgba(228, 23, 23, 0.644);
                border: 0;
                float: right;
            }
            .d1{
                height: 70px;
                border: 1px solid;
                background-color: black;
                display: none;
                border-bottom: 10px solid rgb(146, 37, 209);
                background-color: rgb(0, 0, 0);
            }
            span{font-size: 15px;}
            .ville,.pays{
                text-shadow: 0 0 20px rgb(255, 255, 255);
                color: rgb(255, 255, 255);
                margin-top: 10px;
                margin-left: 30px;
                display: inline-block;
                font-weight: bold;
                font-size: 20px;
                text-transform: uppercase;
            }
            .vilee{
                /* width: 40%; */
                text-align: center;
            }

            @media screen and (max-width:400px) {
                input[type="submit"]{
                    display: none;
                }
                .plc{
                    width: 10px;
                }
                form{
                    width: 35%;
                    padding: 5px;
                }
            }
        </style>
    </head>
    <body>
        <header>
            <div class="tt">Tous les pays du monde et la capitale respective</div>
            <nav>
                <a href="https://github.com/Tostenn" title="my github"><div class="logo">T_xOx_T</div></a>
                <form name="form">
                    <input type="search" name="rech" placeholder="une lettre" id="rech">
                    <input type="submit" value="recherche">
                </form>
                <a class="aide" href="mailto:kouyatosten@gmail.com">aide</a>
            </nav>
        </header>
    <div class="esp"></div>
        <article class="all">
    '''
    
    with open(name,'w') as f:

        for i,j in data.items():
            html += f'''\n     <div class="d1">
        <div class="pays">{i}</div>
        <div class="ville">{j}</div>
    </div>
'''
            
        html += '''    </article>
    <script>
        const article = document.querySelector('.all')
        const div = document.querySelectorAll('.d1')
        const tt = document.querySelector('.tt')
        const pays = document.querySelectorAll('.pays')
        const rech = document.getElementById('rech')
        const list = ['tous']
        rech.onkeyup = ()=>{
        try{
            let data = rech.value.toLowerCase()
            let compte = 0
            lett = "0123456789 "
            if(list.includes(data)){
                if (data == 'tous'){
                    for(let i in div){
                        div[i].style.display = "block"
                    }
                }
            }
            else{
                for(let i in div){
                    div[i].style.display = "none"
                veri = pays[i]
                .innerHTML
                .toLowerCase()
                .includes(data)

                veri1 = lett.includes(data)

                if (veri && veri1 ==false ){
                    setTimeout(() => {
                        div[i].style.display = "block"
                    }, 100);
                }
            }}
            
    }
    catch{0}
        }
        
        let h = innerWidth
        console.log(h);
        h <600 ? tt.innerHTML = 'Welcome':0
        // setInterval(() => {
        // }, 2000);
    </script>
    <footer>
        <!--  -->
    </footer>
</body>
</html>
'''

        f.write(html)
    return True