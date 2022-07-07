import typer
import password
import username
import sens_dir 
import server_detect
import files_info
import login_portals


app = typer.Typer(help="Google Dork Automation Tool")


@app.command()

def urltoscan(url: str = typer.Argument( help="URL for enumeration", default=None), filter: int = typer.Argument(help="Filter number: 1...8", default=None)):
    
    
    print("")
    print(f"Enumerated URL:  {url}")
    print("")
    match filter:
        case 1:       
            username.filter1(url)

        case 2: 
            password.filter2(url)

        case 3: 
            sens_dir.filter3(url)

        case 4:
            server_detect.filter4(url)

        case 5:      
            files_info.filter5(url)

        case 6: 
            login_portals.filter6(url)



if __name__ == "__main__":
    
    banner = ''' 
 
░██████╗░░█████╗░░█████╗░░██████╗░██╗░░░░░███████╗  ██████╗░░█████╗░██████╗░██╗░░██╗
██╔════╝░██╔══██╗██╔══██╗██╔════╝░██║░░░░░██╔════╝  ██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
██║░░██╗░██║░░██║██║░░██║██║░░██╗░██║░░░░░█████╗░░  ██║░░██║██║░░██║██████╔╝█████═╝░
██║░░╚██╗██║░░██║██║░░██║██║░░╚██╗██║░░░░░██╔══╝░░  ██║░░██║██║░░██║██╔══██╗██╔═██╗░
╚██████╔╝╚█████╔╝╚█████╔╝╚██████╔╝███████╗███████╗  ██████╔╝╚█████╔╝██║░░██║██║░╚██╗
░╚═════╝░░╚════╝░░╚════╝░░╚═════╝░╚══════╝╚══════╝  ╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝

 ░█████╗░██╗░░░██╗████████╗░█████╗░███╗░░░███╗░█████╗░████████╗██╗░█████╗░███╗░░██╗
 ██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗████╗░████║██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║
 ███████║██║░░░██║░░░██║░░░██║░░██║██╔████╔██║███████║░░░██║░░░██║██║░░██║██╔██╗██║
 ██╔══██║██║░░░██║░░░██║░░░██║░░██║██║╚██╔╝██║██╔══██║░░░██║░░░██║██║░░██║██║╚████║
 ██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝██║░╚═╝░██║██║░░██║░░░██║░░░██║╚█████╔╝██║░╚███║
 ╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝
    
                    Made By: Muhammad Hazriq Haiqal bin Azhar  

            '''
    GREEN, RED = '\033[1;32m', '\033[91m'

    print(GREEN + banner)
    app()