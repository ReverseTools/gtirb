#include <gtirb/EA.hpp>
#include <sstream>

using namespace gtirb;

EA::EA(uint64_t x) : ea(x)
{
}

void EA::set(uint64_t x)
{
	this->ea = x;
}

uint64_t EA::get() const
{
	return this->ea;
}

EA EA::operator=(EA x)
{
	this->ea = x.ea;
	return *this;
}

bool EA::operator==(uint64_t x) const
{
	return this->ea == x; 
}

bool EA::operator==(EA x) const
{
	return this->ea == x.ea; 
}

bool EA::operator!=(EA x) const
{
	return this->ea != x.ea; 
}

bool EA::operator>(EA x) const
{
	return this->ea > x.ea; 
}

bool EA::operator<(EA x) const
{
	return this->ea < x.ea; 
}

EA EA::operator+(EA x) const
{
	return EA(this->ea + x.ea); 
}

EA EA::operator+=(EA x)
{
	return EA(this->ea += x.ea); 
}

EA EA::operator-(EA x) const
{
	return EA(this->ea - x.ea); 
}

EA EA::operator-=(EA x)
{
	return EA(this->ea -= x.ea); 
}

EA::operator std::string() const
{
	std::stringstream ss;
	ss << std::hex << this->ea;
	return ss.str();
}