from numpy import pi, isnan
from periodictable import formula
from periodictable import Cu,Mo,Ni,Fe,Si
from periodictable.xsf import xray_energy, xray_sld_from_atoms, xray_sld

def test():

    # Check some K_alpha and K_beta1 values
    assert Cu.K_alpha == 1.5418
    assert Cu.K_beta1 == 1.3922

    # Check scalar scattering factor lookup
    f1,f2 = Ni.xray.scattering_factors(xray_energy(Cu.K_alpha))
    assert abs(f1-25.0229)<0.0001
    assert abs(f2-0.5249)<0.0001

    # Check array scattering factor lookup
    f1,f2 = Ni.xray.scattering_factors(xray_energy(Cu.K_alpha))
    m1,m2 = Ni.xray.scattering_factors(xray_energy(Mo.K_alpha))
    B1,B2 = Ni.xray.scattering_factors(xray_energy([Cu.K_alpha,Mo.K_alpha]))
    assert (B1==[f1,m1]).all() and (B2==[f2,m2]).all()

    # Check that we can lookup sld by wavelength and energy
    Fe_rho,Fe_mu = Fe.xray.sld(wavelength=Cu.K_alpha)
    assert abs(Fe_rho-59.45) < 0.01
    Si_rho,Si_mu = Si.xray.sld(energy=8.050)
    assert abs(Si_rho-20.0701) < 0.0001
    assert abs(Si_mu-0.4572) < 0.0001

    # Check that wavelength is the default
    Fe_rho_default,Fe_mu_default = Fe.xray.sld(Cu.K_alpha)
    assert Fe_rho == Fe_rho_default and Fe_mu == Fe_mu_default

    # Check array form of sld lookup
    f1,f2 = Si.xray.sld(wavelength=Cu.K_alpha)
    m1,m2 = Si.xray.sld(wavelength=Mo.K_alpha)
    B1,B2 = Si.xray.sld(wavelength=[Cu.K_alpha,Mo.K_alpha])
    assert (B1==[f1,m1]).all() and (B2==[f2,m2]).all()

    #print Cu.xray.sftable
    #plot_xsf(Cu)
    #emission_table()
    #sld_table(table,Cu.K_alpha)

    """
    # Table of scattering length densities for various molecules
    for molecule,density in [('SiO2',2.2),('B4C',2.52)]:
        atoms = formula(molecule).atoms
        rho,mu = xray_sld(atoms,density,wavelength=Cu.K_alpha)
        print "sld for %s(%g g/cm**3)  rho=%.4g mu=%.4g"\
            %(molecule,density,rho,mu)
    """

    # Cross check against mo
    rho,mu = xray_sld({Si:1},density=Si.density,wavelength=1.54)
    rhoSi,muSi = Si.xray.sld(wavelength=1.54)
    assert abs(rho - rhoSi) < 1e-14
    assert abs(mu - muSi) < 1e-14

    # Check that neutron_sld works as expected
    atoms = formula('SiO2').atoms
    rho,mu = xray_sld(atoms,2.2,energy=xray_energy(Cu.K_alpha))
    assert abs(rho-18.87)<0.1
    atoms = formula('B4C').atoms
    rho,mu = xray_sld(atoms,2.52,energy=xray_energy(Cu.K_alpha))
    assert abs(rho-20.17)<0.1

    rho,mu = xray_sld('', density=0, wavelength=Cu.K_alpha)
    assert rho==mu==0

    # Check f0 calculation for scalar, vector, array and empty
    Q1,Q2 = 4*pi/Cu.K_alpha, 4*pi/Mo.K_alpha
    f0 = Ni.xray.f0(Q=Q1)
    assert abs(f0-10.11303) < 0.00001
    assert isnan(Ni.xray.f0(Q=7*4*pi))

    f0 = Ni.xray.f0(Q=Q1)
    m0 = Ni.xray.f0(Q=Q2)
    B0 = Ni.xray.f0(Q=[Q1,Q2])
    assert (B0==[f0,m0]).all()


    f0 = Ni.xray.f0(Q=[])
    assert len(f0) == 0

    f0 = Ni.xray.f0(Q=[[1,2],[3,4]])
    assert f0[0,0] == Ni.xray.f0(1)
    assert f0[0,1] == Ni.xray.f0(2)
    assert f0[1,0] == Ni.xray.f0(3)
    assert f0[1,1] == Ni.xray.f0(4)

    # Check f0 calculation for ion
    Ni_2p_f0 = Ni.ion[2].xray.f0(Q=Q1)
    assert abs(Ni_2p_f0-10.09535) < 0.00001
    Ni58_2p_f0 = Ni[58].ion[2].xray.f0(Q=Q1)
    assert Ni_2p_f0 == Ni58_2p_f0
    
    # The following test is implementation specific, and is not guaranteed
    # to succeed if the extension interface changes.
    assert '_xray' not in Ni[58].__dict__

if __name__ == "__main__": test()