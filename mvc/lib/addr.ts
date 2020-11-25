export class Addr {
	name: string;
	addr: string;
	ipaddr: string;
}

export class AddrView {
　　id: number;
	name: string;
	addr: string;
	ipaddr: string;
}

export interface AddrsType {
	StatusCode: number,
	ErrorCode: string,
	Result: AddrView[]
}

export default Addr;