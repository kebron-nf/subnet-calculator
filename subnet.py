import ipaddress
import random
import sys

# ANSI Color Codes for terminal styling
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

def print_banner():
    print(f"{Colors.CYAN}{Colors.BOLD}")
    print("╔══════════════════════════════════════════════════╗")
    print("║             ULTIMATE PYTHON SUBNET TOOL          ║")
    print("║         [ Calculator, Splitter & Quiz ]          ║")
    print("╚══════════════════════════════════════════════════╝")
    print(f"{Colors.RESET}")

def decimal_to_binary(ip_str):
    """Converts an IP or subnet mask string into its 8-bit binary representation."""
    octets = ip_str.split('.')
    binary_octets = [bin(int(octet))[2:].zfill(8) for octet in octets]
    return '.'.join(binary_octets)

def calculate_single(ip_cidr):
    try:
        network = ipaddress.ip_network(ip_cidr, strict=False)
        net_address = str(network.network_address)
        net_mask = str(network.netmask)
        broadcast = str(network.broadcast_address)
        cidr = network.prefixlen
        total_ips = network.num_addresses
        
        hosts = list(network.hosts())
        if hosts:
            first_usable = str(hosts[0])
            last_usable = str(hosts[-1])
            usable_count = len(hosts)
        else:
            first_usable = "N/A"
            last_usable = "N/A"
            usable_count = 0

        print(f"\n{Colors.GREEN}{Colors.BOLD}[+] ANALYSIS FOR: {ip_cidr}{Colors.RESET}")
        print(f"{Colors.YELLOW}──────────────────────────────────────────────{Colors.RESET}")
        print(f"  {Colors.BOLD}Network ID      :{Colors.RESET} {net_address}")
        print(f"  {Colors.BOLD}Binary Net ID   :{Colors.RESET} {Colors.BLUE}{decimal_to_binary(net_address)}{Colors.RESET}")
        print(f"  {Colors.BOLD}Subnet Mask     :{Colors.RESET} {net_mask}")
        print(f"  {Colors.BOLD}Binary Mask     :{Colors.RESET} {Colors.BLUE}{decimal_to_binary(net_mask)}{Colors.RESET}")
        print(f"  {Colors.BOLD}CIDR Notation   :{Colors.RESET} /{cidr}")
        print(f"  {Colors.BOLD}Broadcast ID    :{Colors.RESET} {broadcast}")
        print(f"  {Colors.BOLD}Total IPs       :{Colors.RESET} {total_ips}")
        print(f"  {Colors.BOLD}Usable Hosts    :{Colors.RESET} {usable_count}")
        print(f"  {Colors.BOLD}Usable Range    :{Colors.RESET} {Colors.GREEN}{first_usable}  to  {last_usable}{Colors.RESET}")
        print(f"{Colors.YELLOW}──────────────────────────────────────────────{Colors.RESET}\n")

    except ValueError:
        print(f"\n{Colors.RED}[!] Error: Invalid IP address or CIDR format. (e.g., 10.200.20.0/27){Colors.RESET}\n")

def split_network(ip_cidr, num_subnets):
    try:
        parent_net = ipaddress.ip_network(ip_cidr, strict=False)
        bits_to_borrow = 0
        while (2 ** bits_to_borrow) < num_subnets:
            bits_to_borrow += 1
            
        new_cidr = parent_net.prefixlen + bits_to_borrow
        
        if new_cidr > 32:
            print(f"\n{Colors.RED}[!] Error: Too many subnets requested for this network size!{Colors.RESET}\n")
            return

        subnets = list(parent_net.subnets(new_prefix=new_cidr))
        
        print(f"\n{Colors.GREEN}{Colors.BOLD}[+] SPLITTING {ip_cidr} INTO {num_subnets} SUBNETS (Using /{new_cidr}):{Colors.RESET}")
        print(f"{Colors.YELLOW}──────────────────────────────────────────────{Colors.RESET}")
        
        for i, sub in enumerate(subnets[:num_subnets], 1):
            hosts = list(sub.hosts())
            first_usable = str(hosts[0]) if hosts else "N/A"
            last_usable = str(hosts[-1]) if hosts else "N/A"
            net_addr_str = str(sub.network_address)
            mask_str = str(sub.netmask)
            
            print(f"  {Colors.CYAN}Subnet {i}:{Colors.RESET}")
            print(f"    Network ID    : {net_addr_str}/{new_cidr}")
            print(f"    Binary Net ID : {Colors.BLUE}{decimal_to_binary(net_addr_str)}{Colors.RESET}")
            print(f"    Subnet Mask   : {mask_str}")
            print(f"    Binary Mask   : {Colors.BLUE}{decimal_to_binary(mask_str)}{Colors.RESET}")
            print(f"    CIDR Notation : /{new_cidr}")
            print(f"    Total IPs     : {sub.num_addresses}")
            print(f"    Usable Hosts  : {len(hosts)}")
            print(f"    Usable Range  : {Colors.GREEN}{first_usable} to {last_usable}{Colors.RESET}")
            print(f"    Broadcast     : {sub.broadcast_address}")
            print(f"    ------------------------------------------")
            
        print(f"{Colors.YELLOW}──────────────────────────────────────────────{Colors.RESET}\n")

    except ValueError as e:
        print(f"\n{Colors.RED}[!] Error: {e}{Colors.RESET}\n")

def run_quiz():
    print(f"\n{Colors.HEADER}{Colors.BOLD}=== SUBNETTING QUIZ MODE ==={Colors.RESET}")
    print(f"{Colors.CYAN}Test your skills! Type 'q' anytime to exit the quiz.{Colors.RESET}\n")
    
    score = 0
    total_questions = 0
    
    # Pool of random base networks and target questions
    mock_ips = ["192.168.1.0", "10.0.0.0", "172.16.10.0", "192.168.100.0"]
    cidrs = [24, 25, 26, 27, 28, 29]
    
    while True:
        base_ip = random.choice(mock_ips)
        cidr = random.choice(cidrs)
        net_str = f"{base_ip}/{cidr}"
        net = ipaddress.ip_network(net_str, strict=False)
        
        question_type = random.choice(["broadcast", "mask", "usable_hosts"])
        
        if question_type == "broadcast":
            correct_ans = str(net.broadcast_address)
            prompt = f"What is the {Colors.BOLD}Broadcast IP{Colors.RESET} for {Colors.GREEN}{net_str}{Colors.RESET}?: "
        elif question_type == "mask":
            correct_ans = str(net.netmask)
            prompt = f"What is the decimal {Colors.BOLD}Subnet Mask{Colors.RESET} for {Colors.GREEN}{net_str}{Colors.RESET}?: "
        else:
            hosts = list(net.hosts())
            correct_ans = str(len(hosts))
            prompt = f"How many {Colors.BOLD}Usable Hosts{Colors.RESET} are in {Colors.GREEN}{net_str}{Colors.RESET}?: "
            
        user_ans = input(prompt).strip()
        
        if user_ans.lower() == 'q':
            print(f"\n{Colors.YELLOW}Quiz ended! Your final score: {score}/{total_questions}{Colors.RESET}\n")
            break
            
        total_questions += 1
        if user_ans == correct_ans:
            score += 1
            print(f"{Colors.GREEN}[✔] Correct! Awesome job, bro.{Colors.RESET}\n")
        else:
            print(f"{Colors.RED}[✖] Wrong! The correct answer was: {correct_ans}{Colors.RESET}\n")

def main():
    print_banner()
    
    while True:
        print(f"{Colors.HEADER}Choose an option:{Colors.RESET}")
        print(f"  {Colors.CYAN}1){Colors.RESET} Single Network Analysis (with Binary & Hosts)")
        print(f"  {Colors.CYAN}2){Colors.RESET} Split Network into Smaller Subnets")
        print(f"  {Colors.CYAN}3){Colors.RESET} Subnet Quiz Mode (Test Yourself)")
        print(f"  {Colors.CYAN}4){Colors.RESET} Exit tool")
        
        choice = input(f"\n{Colors.BOLD}Enter your choice [1-4]: {Colors.RESET}").strip()
        
        if choice == '1':
            user_input = input(f"{Colors.BOLD}Enter IP with CIDR (e.g., 10.200.20.0/27): {Colors.RESET}").strip()
            calculate_single(user_input)
            
        elif choice == '2':
            user_input = input(f"{Colors.BOLD}Enter Parent IP with CIDR (e.g., 10.200.20.0/27): {Colors.RESET}").strip()
            try:
                sub_count = int(input(f"{Colors.BOLD}How many subnets do you want? (e.g., 2,3,4,5 or 6): {Colors.RESET}").strip())
                split_network(user_input, sub_count)
            except ValueError:
                print(f"\n{Colors.RED}[!] Please enter a valid number for subnets.{Colors.RESET}\n")
                
        elif choice == '3':
            run_quiz()
            
        elif choice == '4':
            print(f"\n{Colors.GREEN}Exiting tool. Keep crushing it, bro!{Colors.RESET}\n")
            break
        else:
            print(f"\n{Colors.RED}[!] Invalid option. Please choose 1, 2, 3, or 4.{Colors.RESET}\n")

if __name__ == "__main__":
    main()
